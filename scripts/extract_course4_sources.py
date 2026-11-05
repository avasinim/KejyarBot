#!/usr/bin/env python3
"""Extract the two approved Course 4 PDFs for source review.

Embedded PDF text is preferred and preserved verbatim as far as PyMuPDF allows.
OCR is only a fallback for pages with almost no extractable text. OCR output is
explicitly marked so it cannot be mistaken for verified source transcription.
"""
from __future__ import annotations

import json
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "source-extract" / "course4"
SOURCES = (
    ("Rezmany_axawtny_kurdy.pdf", "01_rezmany_axawtny_kurdy.txt"),
    ("ڕێزمانی ڕاناوی لكاو.pdf", "02_rezmany_ranawy_lkaw.txt"),
)


def page_text(page: fitz.Page) -> tuple[str, str]:
    text = page.get_text("text", sort=False).strip()
    if len("".join(text.split())) >= 25:
        return text, "embedded-text"

    pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    try:
        ocr = pytesseract.image_to_string(image, lang="ara+eng", config="--psm 6").strip()
    except pytesseract.TesseractError as exc:
        return text, f"ocr-failed: {exc}"
    if ocr:
        return ocr, "OCR-ara+eng-UNVERIFIED"
    return text, "no-readable-text"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report = []
    for source_name, output_name in SOURCES:
        source = ROOT / source_name
        if not source.is_file():
            raise FileNotFoundError(f"Required source PDF missing: {source_name}")

        doc = fitz.open(source)
        blocks = []
        methods = []
        for page_number, page in enumerate(doc, start=1):
            content, method = page_text(page)
            methods.append(method)
            blocks.append(
                f"\n\n===== پەڕەی {page_number} | {method} =====\n\n{content}"
            )

        destination = OUT / output_name
        destination.write_text(
            f"سەرچاوە: {source_name}\n"
            "تێبینی: دەقی OCR پشتڕاستکراوە نییە و پێویستی بە بەراوردی دەستی لەگەڵ PDF هەیە.\n"
            + "".join(blocks),
            encoding="utf-8",
        )
        report.append({
            "source": source_name,
            "pages": len(doc),
            "output": str(destination.relative_to(ROOT)),
            "embedded_text_pages": methods.count("embedded-text"),
            "ocr_pages": sum(m.startswith("OCR-") for m in methods),
            "unreadable_pages": sum(m == "no-readable-text" for m in methods),
            "page_methods": methods,
        })

    (OUT / "extraction_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
