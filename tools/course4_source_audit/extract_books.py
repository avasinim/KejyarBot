import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path
import fitz

SOURCES = [
    (1, "2fb363f0abf3ebd4e753bd71f7c3d22d97cb7f55", "بەرگی ١ حا.pdf", "6a7153f0e50aee37f7f75bf0ab7c5faee5e1dd96"),
    (2, "0b6c2941afcf91fe88c6c4b44ff954bb543f04cb", "بەرگی ٢.pdf", "c59e2f80004685aab85df203d6f5564deff62d6a"),
    (3, "c20d44b7c4833e28eda51702e17d430816ef72b3", "بەرگی ٣.pdf", "810aac877c8422924db41db4d0ea4aaf96d53dce"),
    (4, "e12112f4a9c7ebd6006a3089871aabc835e4a3d3", "بەرگی ٤.PDF", "322fd56eb9f0aa18df1c94ecb89fd4b774dd6234"),
    (5, "45166d71ba9ccaa3caf320e7edf334b95fa91044", "بەرگی ٥.pdf", "001a3fd91ba07f85cac1e5ac3214725241a72f7e"),
]

def main():
    out = Path("audit-output")
    out.mkdir(exist_ok=True)
    manifest = []
    for number, commit, filename, expected in SOURCES:
        path = urllib.parse.quote(filename, safe="")
        url = f"https://raw.githubusercontent.com/avasinim/KejyarBot/{commit}/{path}"
        request = urllib.request.Request(url, headers={"User-Agent": "KejyarBot-Course4-Audit"})
        data = urllib.request.urlopen(request, timeout=120).read()
        actual = hashlib.sha1(f"blob {len(data)}\\0".encode() + data).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Blob SHA mismatch for volume {number}")
        pdf = fitz.open(stream=data, filetype="pdf")
        page_data = []
        for index, page in enumerate(pdf, start=1):
            text = " ".join(page.get_text("text").split())
            page_data.append({"page": index, "characters": len(text), "has_text": len(text) > 70})
        manifest.append({"volume": number, "filename": filename, "commit": commit,
                         "blob_sha_verified": actual, "bytes": len(data),
                         "pdf_pages": len(pdf), "page_index": page_data})
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
