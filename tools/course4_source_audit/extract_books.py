import csv
import hashlib
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

SOURCES = [
    (1, "2fb363f0abf3ebd4e753bd71f7c3d22d97cb7f55", "بەرگی ١ حا.pdf", "6a7153f0e50aee37f7f75bf0ab7c5faee5e1dd96",
     {"1":["پێزمان","مۆرفۆلۆژی","سینتاکس"],"2":["ناوی تایبەتی","ناوی گشتی","کۆمەڵ"],"3":["مادی","مەعنەوی"],"4":["سادە","ناسادە","ڕەگەز"],"5":["ژمارە","ناسیاوی","نەناسیاوی"],"6":["ڕستە","شیکردنەوە"]}),
    (2, "0b6c2941afcf91fe88c6c4b44ff954bb543f04cb", "بەرگی ٢.pdf", "c59e2f80004685aab85df203d6f5564deff62d6a",
     {"7":["جێناو","ناو"],"8":["کەسی","جێناو"],"9":["خاوەنداری","پەیوەست"],"10":["پرسیاری","نەفی"],"11":["نیشانە","ئاماژە"],"12":["ڕستەسازی","جێناو"]}),
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

def ocr_page(page):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False)
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    try:
        raw = pytesseract.image_to_string(image, lang="ara+eng", config="--psm 6")
    except pytesseract.TesseractError:
        raw = pytesseract.image_to_string(image, lang="ara", config="--psm 6")
    return re.sub(r"\\s+", " ", raw).strip()

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
        for index, page in enumerate(pdf, start=1):
            if index == 1 or index % 25 == 0 or index == len(pdf):
                print(f"Volume {number}: OCR progress {index}/{len(pdf)} pages", flush=True)
            text = " ".join(page.get_text("text").split())
            method = "embedded-text"
            if len(text) < 70:
                text = ocr_page(page)
                method = "ocr-ara"
                ocr_count += 1
            else:
                embedded_count += 1
            extracted.append(text)
            page_rows.append({"volume":number,"pdf_page":index,"characters":len(text),
                              "method":method,"needs_visual_check":"yes" if len(text)<70 else "no"})
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
