# save as make_pdf_zip.py
import os, zipfile, argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--src", required=True, help="root folder with class subfolders")
parser.add_argument("--out", default="pdfs_labeled.zip")
args = parser.parse_args()

with zipfile.ZipFile(args.out, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for cls in sorted(os.listdir(args.src)):
        cdir = Path(args.src)/cls
        if not cdir.is_dir(): continue
        for p in cdir.rglob("*.pdf"):
            z.write(p, arcname=str(Path(cls)/p.name))
print(f"Wrote {args.out}")
