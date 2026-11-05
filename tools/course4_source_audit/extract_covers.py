import hashlib
import urllib.parse
import urllib.request
from pathlib import Path

import fitz
import pytesseract
from PIL import Image, ImageOps, ImageDraw

SOURCES = [
    (1, "2fb363f0abf3ebd4e753bd71f7c3d22d97cb7f55", "بەرگی ١ حا.pdf", "6a7153f0e50aee37f7f75bf0ab7c5faee5e1dd96"),
    (2, "0b6c2941afcf91fe88c6c4b44ff954bb543f04cb", "بەرگی ٢.pdf", "c59e2f80004685aab85df203d6f5564deff62d6a"),
    (3, "c20d44b7c4833e28eda51702e17d430816ef72b3", "بەرگی ٣.pdf", "810aac877c8422924db41db4d0ea4aaf96d53dce"),
    (4, "e12112f4a9c7ebd6006a3089871aabc835e4a3d3", "بەرگی ٤.PDF", "322fd56eb9f0aa18df1c94ecb89fd4b774dd6234"),
    (5, "45166d71ba9ccaa3caf320e7edf334b95fa91044", "بەرگی ٥.pdf", "001a3fd91ba07f85cac1e5ac3214725241a72f7e"),
]

def verify(data, expected):
    header = b"blob " + str(len(data)).encode() + bytes.fromhex("00")
    actual = hashlib.sha1(header + data).hexdigest()
    if actual != expected:
        raise RuntimeError(f"Git blob mismatch: {actual}")
    return actual

def main():
    out = Path("cover-audit")
    out.mkdir(exist_ok=True)
    summary = []
    for number, commit, filename, expected in SOURCES:
        url = f"https://raw.githubusercontent.com/avasinim/KejyarBot/{commit}/{urllib.parse.quote(filename, safe='')}"
        req = urllib.request.Request(url, headers={"User-Agent": "KejyarBot-Course4-Cover-Audit"})
        data = urllib.request.urlopen(req, timeout=90).read()
        blob = verify(data, expected)
        pdf = fitz.open(stream=data, filetype="pdf")
        pages = []
        texts = []
        for i, page in enumerate(list(pdf)[:5], start=1):
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
            im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pages.append(im)
            try:
                txt = pytesseract.image_to_string(im, lang="ara+eng", config="--psm 6", timeout=20)
            except Exception as exc:
                txt = f"[OCR unavailable: {type(exc).__name__}]"
            texts.append(f"VOLUME {number} — PDF PAGE {i}\n{txt.strip()}\n")
        # One contact sheet per volume, for direct visual inspection.
        thumbs = []
        for im in pages:
            im.thumbnail((900, 1250))
            canvas = Image.new("RGB", (920, 1300), "white")
            canvas.paste(im, ((920-im.width)//2, 35))
            thumbs.append(canvas)
        sheet = Image.new("RGB", (920 * len(thumbs), 1300), "#dddddd")
        for idx, im in enumerate(thumbs):
            sheet.paste(im, (idx*920, 0))
        sheet.save(out / f"volume-{number}-first-five-pages.jpg", quality=88)
        (out / f"volume-{number}-ocr.txt").write_text("\n".join(texts), encoding="utf-8")
        summary.append(f"Volume {number}: pages={len(pdf)}, verified_blob={blob}, bytes={len(data)}")
    (out / "manifest.txt").write_text("\n".join(summary), encoding="utf-8")
    print("\n".join(summary))
    print("Bounded cover audit complete: first five pages per volume only.")

if __name__ == "__main__":
    main()
