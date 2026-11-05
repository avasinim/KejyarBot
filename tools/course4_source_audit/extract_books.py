import csv
import hashlib
import json
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

# Provisional source ordering: Volume 1 is directly cover-verified as Part 2 (Pronoun).
# Volume 2 is strongly matched to Part 1 (Noun) by the independent catalogue's
# 23.30 MB / 304-page record vs this repository PDF's 24,426,929 bytes.
# Keep the hard stop in main() until Volume 2's own cover is visually verified.
SOURCES = [
    (1, "2fb363f0abf3ebd4e753bd71f7c3d22d97cb7f55", "بەرگی ١ حا.pdf", "6a7153f0e50aee37f7f75bf0ab7c5faee5e1dd96",
     {"7":["جێناو","کەسی"],"8":["واتا","تایبەتمەندی جێناو"],"9":["جێناوی کەسی","خاوەنداری"],"10":["پرسیاری","نەفی"],"11":["نیشانە","ئاماژە"],"12":["ڕستەسازی","پێکهاتەسازی"]}),
    (2, "0b6c2941afcf91fe88c6c4b44ff954bb543f04cb", "بەرگی ٢.pdf", "c59e2f80004685aab85df203d6f5564deff62d6a",
     {"1":["ناو","ناوی تایبەتی","ناوی گشتی"],"2":["کۆمەڵ","ناوی کۆ"],"3":["مادی","مەعنەوی"],"4":["سادە","لێکدراو","ڕەگەز"],"5":["ژمارە","ناسیاوی","نەناسیاوی"],"6":["ڕستە","شیکردنەوە"]}),
    (3, "c20d44b7c4833e28eda51702e17d430816ef72b3", "بەرگی ٣.pdf", "810aac877c8422924db41db4d0ea4aaf96d53dce",
     {"13":["ئاوەڵناو","ناو"],"14":["چۆنیەتی","نسبی","سادە","لێکدراو"],"15":["پلە","بەراورد","superlativus"],"16":["پاشگر","ڕەگەز","ژمارە"],"17":["دەربڕین","ڕستە"],"18":["ئاوەڵناو","شیکردنەوە"]}),
    (4, "e12112f4a9c7ebd6006a3089871aabc835e4a3d3", "بەرگی ٤.PDF", "322fd56eb9f0aa18df1c94ecb89fd4b774dd6234",
     {"19":["ژمارە","بنجی","پەلەیی","کەرتی","دایەش"],"20":["ژمارەی بنجی","تاک","کۆ"],"21":["پەلەیی","کەرتی","دایەش"],"22":["ئاوەڵکردار","پۆلی وشە"],"23":["ئاوەڵکردار","واتا","ڕستەسازی"],"24":["ئاوەڵناو","ئاوەڵکردار"]}),
    (5, "45166d71ba9ccaa3caf320e7edf334b95fa91044", "بەرگی ٥.pdf", "001a3fd91ba07f85cac1e5ac3214725241a72f7e",
     {"25":["دەنگ","وشەڕۆنان","وشەسازی","ڕستەسازی"],"26":["چاوگ","ڕەگ","قەد","پێشگر","پاشگر"],"27":["کەس","ژمارە","کات","ڕیزە"],"28":["تێپەڕ","ناتێپەڕ","بەرکار"],"29":["کارا دیار","کارا بڕزی","اندن"],"30":["سادە","ناسادە","ئەرێنی","نەرێنی"]}),
]

def verify_git_blob(data, expected):
    header = b"blob " + str(len(data)).encode() + bytes.fromhex("00")
    actual = hashlib.sha1(header + data).hexdigest()
    if actual != expected:
        raise RuntimeError("Git blob SHA mismatch: " + actual)
    return actual

def render_page(page):
    pix = page.get_pixmap(matrix=fitz.Matrix(0.9, 0.9), alpha=False)
    return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

def ocr_image(image):
    try:
        raw = pytesseract.image_to_string(
            image, lang="ara+eng", config="--psm 6", timeout=12
        )
    except (pytesseract.TesseractError, RuntimeError):
        try:
            raw = pytesseract.image_to_string(
                image, lang="ara", config="--psm 6", timeout=8
            )
        except (pytesseract.TesseractError, RuntimeError):
            return ""
    return re.sub(r"\s+", " ", raw).strip()

def short_excerpt(text, terms, limit=28):
    words = text.split()
    if not words:
        return ""
    lower = text.lower()
    positions = [lower.find(term.lower()) for term in terms if lower.find(term.lower()) >= 0]
    if positions:
        first = min(positions)
        start = max(0, len(text[:first].split()) - 8)
        return " ".join(words[start:start + limit])
    return " ".join(words[:limit])

def main():
    raise RuntimeError(
        "Unsafe source mapping: Volume 1 cover is Part 2 (Pronoun), not Part 1 (Noun). "
        "Do not run lesson-page matching until all five printed covers are verified "
        "and SOURCES lesson mappings are corrected. Use extract_covers.py only."
    )
    out = Path("audit-output")
    out.mkdir(exist_ok=True)
    manifests, page_rows, lesson_rows = [], [], []
    for number, commit, filename, expected, lessons in SOURCES:
        encoded = urllib.parse.quote(filename, safe="")
        url = f"https://raw.githubusercontent.com/avasinim/KejyarBot/{commit}/{encoded}"
        request = urllib.request.Request(url, headers={"User-Agent":"KejyarBot-Course4-Audit"})
        data = urllib.request.urlopen(request, timeout=180).read()
        verified = verify_git_blob(data, expected)
        pdf = fitz.open(stream=data, filetype="pdf")
        extracted = []
        embedded_count = 0
        ocr_count = 0
        with ThreadPoolExecutor(max_workers=4) as pool:
            pages = list(pdf)
            for batch_start in range(0, len(pages), 4):
                batch = pages[batch_start:batch_start + 4]
                batch_meta = []
                images = []
                for offset, page in enumerate(batch):
                    index = batch_start + offset + 1
                    text = " ".join(page.get_text("text").split())
                    if len(text) >= 70:
                        batch_meta.append((index, text, "embedded-text"))
                        embedded_count += 1
                    else:
                        images.append(render_page(page))
                        batch_meta.append((index, None, "ocr-ara"))
                ocr_images = list(images)
                if ocr_images:
                    ocr_texts = list(pool.map(ocr_image, ocr_images))
                    text_iter = iter(ocr_texts)
                    rebuilt = []
                    for index, text, method in batch_meta:
                        if method == "ocr-ara":
                            text = next(text_iter)
                            ocr_count += 1
                        rebuilt.append((index, text, method))
                    batch_meta = rebuilt
                for index, text, method in batch_meta:
                    extracted.append(text)
                    page_rows.append({"volume":number,"pdf_page":index,"characters":len(text),
                                      "method":method,"needs_visual_check":"yes" if len(text)<70 else "no"})
                    if index == 1 or index % 10 == 0 or index == len(pdf):
                        print(f"Volume {number}: OCR progress {index}/{len(pdf)} pages", flush=True)
        for lesson, terms in lessons.items():
            scored = []
            for page_no, text in enumerate(extracted, start=1):
                score = sum(1 for term in terms if term.lower() in text.lower())
                if score:
                    scored.append((score, page_no, text))
            if scored:
                score, page_no, text = max(scored, key=lambda row: (row[0], len(row[2])))
                excerpt = short_excerpt(text, terms)
            else:
                page_no, score, excerpt = "", 0, "هیچ هاوتایەکی OCR نەدۆزرایەوە؛ پشکنینی وێنەیی پێویستە."
            lesson_rows.append({"volume":number,"lesson":lesson,"pdf_page":page_no,
                                "matched_terms":score,"search_terms":"، ".join(terms),
                                "short_excerpt":excerpt})
        manifests.append({"volume":number,"filename":filename,"commit":commit,
                          "blob_sha_verified":verified,"bytes":len(data),"pdf_pages":len(pdf),
                          "embedded_text_pages":embedded_count,"ocr_pages":ocr_count})
    (out/"volume_manifest.json").write_text(json.dumps(manifests,ensure_ascii=False,indent=2),encoding="utf-8")
    with (out/"page_quality_index.csv").open("w",newline="",encoding="utf-8-sig") as f:
        writer=csv.DictWriter(f,fieldnames=["volume","pdf_page","characters","method","needs_visual_check"])
        writer.writeheader()
        writer.writerows(page_rows)
    with (out/"lesson_source_excerpt_index.csv").open("w",newline="",encoding="utf-8-sig") as f:
        writer=csv.DictWriter(f,fieldnames=["volume","lesson","pdf_page","matched_terms","search_terms","short_excerpt"])
        writer.writeheader()
        writer.writerows(lesson_rows)
    print(json.dumps(manifests,ensure_ascii=False,indent=2))
    print("OCR complete. Full book text was not written to the artifact.", flush=True)

if __name__ == "__main__":
    main()
