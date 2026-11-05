#!/usr/bin/env python3
"""Render review contact sheets and readable page images for Course 4 PDFs."""
from pathlib import Path
import json
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "source-extract" / "course4" / "previews"
PAGE_OUT = OUT / "individual_pages"
OUT.mkdir(parents=True, exist_ok=True)
PAGE_OUT.mkdir(parents=True, exist_ok=True)

def render_page(doc, page_no, output):
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(output, format="JPEG", quality=91, optimize=True)

def sheet(pdf_name, pages, prefix):
    doc = fitz.open(ROOT / pdf_name)
    thumb_w, thumb_h, cols = 300, 390, 4
    per_sheet = 16
    for batch_start in range(0, len(pages), per_sheet):
        batch = pages[batch_start:batch_start + per_sheet]
        rows = (len(batch) + cols - 1) // cols
        canvas = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + 28)), "white")
        draw = ImageDraw.Draw(canvas)
        for i, page_no in enumerate(batch):
            page = doc[page_no - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(0.55, 0.55), alpha=False)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            img.thumbnail((thumb_w - 12, thumb_h - 12))
            x = (i % cols) * thumb_w + (thumb_w - img.width) // 2
            y = (i // cols) * (thumb_h + 28) + 24
            canvas.paste(img, (x, y))
            draw.text(((i % cols) * thumb_w + 8, (i // cols) * (thumb_h + 28) + 5),
                      f"PDF page {page_no}", fill="black")
        path = OUT / f"{prefix}_{batch_start // per_sheet + 1:02d}.jpg"
        canvas.save(path, quality=88, optimize=True)

def main():
    suffix_name = "ڕێزمانی ڕاناوی لكاو.pdf"
    main_name = "Rezmany_axawtny_kurdy.pdf"
    suffix_pages = list(range(1, 33))
    # Render the opening pages, the next systematic review block, the adverb/preposition review block, and closing pages.
    # Continue in bounded blocks so artifacts remain practical to inspect.
    main_pages = list(range(1, 81)) + list(range(81, 161)) + list(range(161, 301)) + list(range(301, 380)) + list(range(380, 401))
    sheet(suffix_name, suffix_pages, "suffix_pronouns")
    sheet(main_name, main_pages, "main_grammar")
    for pdf_name, pages, prefix in (
        (suffix_name, suffix_pages, "suffix"),
        (main_name, main_pages, "main"),
    ):
        doc = fitz.open(ROOT / pdf_name)
        for page_no in pages:
            render_page(doc, page_no, PAGE_OUT / f"{prefix}_page_{page_no:03d}.jpg")

    report = {}
    for name in (main_name, suffix_name):
        doc = fitz.open(ROOT / name)
        report[name] = {
            "pages": len(doc),
            "metadata": doc.metadata,
            "fonts_first_12_pages": [
                {"page": n, "fonts": [f[3] for f in doc[n-1].get_fonts(full=True)]}
                for n in range(1, min(12, len(doc)) + 1)
            ],
        }
    (OUT / "pdf_diagnostics.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Rendered contact sheets, individual review pages, and PDF diagnostics.")

if __name__ == "__main__":
    main()
