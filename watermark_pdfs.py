"""
Watermark all SECS Research PDFs with the sovereign seal.

Places a semi-transparent seal image in the bottom-right corner
of every page, plus a text line along the bottom margin.

Usage:  py watermark_pdfs.py [--dry-run]

Originals are backed up to  _originals/  before any modification.
"""

import argparse
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


REPO = Path(__file__).resolve().parent
SEAL_PATH = REPO / "seal.png"
BACKUP_DIR = REPO / "_originals"
WATERMARK_TEXT = "SECS Research  ·  Jay A Carpenter  ·  SECS.Observer"

# Seal dimensions on the page (points). 72 pt = 1 inch.
SEAL_SIZE = 72          # 1 inch square
MARGIN_RIGHT = 28       # from right edge
MARGIN_BOTTOM = 24      # from bottom edge
TEXT_MARGIN_LEFT = 36
TEXT_MARGIN_BOTTOM = 30
TEXT_FONT_SIZE = 7
TEXT_OPACITY = 0.55
SEAL_OPACITY = 0.40

# Cache the pre-shrunk seal as a temp JPEG for fast reportlab embedding
_seal_jpg_path = None

def _prepare_seal():
    """Shrink seal PNG to a small JPEG once for performance."""
    global _seal_jpg_path
    if _seal_jpg_path and os.path.exists(_seal_jpg_path):
        return _seal_jpg_path
    img = Image.open(SEAL_PATH).convert("RGB")
    img.thumbnail((200, 200), Image.LANCZOS)
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    img.save(tmp, format="JPEG", quality=85)
    tmp.close()
    _seal_jpg_path = tmp.name
    return _seal_jpg_path


def make_watermark_page(width: float, height: float) -> bytes:
    """Build a single-page PDF with the seal and text overlay."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(width, height))

    # --- Seal image (bottom-right, semi-transparent) ---
    if SEAL_PATH.exists():
        seal_jpg = _prepare_seal()
        c.saveState()
        c.setFillAlpha(SEAL_OPACITY)
        x = width - SEAL_SIZE - MARGIN_RIGHT
        y = MARGIN_BOTTOM
        c.drawImage(
            seal_jpg,
            x, y,
            width=SEAL_SIZE, height=SEAL_SIZE,
            preserveAspectRatio=True,
        )
        c.restoreState()

    # --- Text line (bottom-left, muted) ---
    c.saveState()
    c.setFillAlpha(TEXT_OPACITY)
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.setFont("Helvetica", TEXT_FONT_SIZE)
    c.drawString(TEXT_MARGIN_LEFT, TEXT_MARGIN_BOTTOM, WATERMARK_TEXT)
    c.restoreState()

    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()


_wm_cache: dict[tuple[int, int], bytes] = {}

def _get_watermark(pw: float, ph: float) -> bytes:
    """Cached watermark page bytes by page dimensions."""
    key = (int(pw), int(ph))
    if key not in _wm_cache:
        _wm_cache[key] = make_watermark_page(pw, ph)
    return _wm_cache[key]


def watermark_pdf(pdf_path: Path, dry_run: bool = False) -> bool:
    """Stamp every page of a single PDF. Returns True on success."""
    # Read entire file into memory so we don't hold a file handle
    try:
        pdf_bytes = pdf_path.read_bytes()
        reader = PdfReader(io.BytesIO(pdf_bytes))
    except Exception as e:
        print(f"  SKIP  {pdf_path.name}  ({e})")
        return False

    if reader.is_encrypted:
        print(f"  SKIP  {pdf_path.name}  (encrypted)")
        return False

    writer = PdfWriter()

    for page in reader.pages:
        box = page.mediabox
        pw = float(box.width)
        ph = float(box.height)

        wm_bytes = _get_watermark(pw, ph)
        wm_reader = PdfReader(io.BytesIO(wm_bytes))
        wm_page = wm_reader.pages[0]

        page.merge_page(wm_page, over=True)
        writer.add_page(page)

    # Copy metadata
    if reader.metadata:
        writer.add_metadata(
            {k: v for k, v in reader.metadata.items() if isinstance(v, str)}
        )

    if dry_run:
        print(f"  DRY   {pdf_path.relative_to(REPO)}")
        return True

    # Backup original
    rel = pdf_path.relative_to(REPO)
    backup = BACKUP_DIR / rel
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_path, backup)

    # Write stamped version to temp file, then replace
    tmp_path = pdf_path.with_suffix(".tmp.pdf")
    with open(tmp_path, "wb") as f:
        writer.write(f)
    tmp_path.replace(pdf_path)

    print(f"  OK    {rel}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Stamp SECS seal on all PDFs")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    if not SEAL_PATH.exists():
        print(f"ERROR: Seal image not found at {SEAL_PATH}")
        sys.exit(1)

    pdfs = sorted(REPO.rglob("*.pdf"))
    # Exclude any in _originals backup dir
    pdfs = [p for p in pdfs if "_originals" not in p.parts]

    print(f"\nSECS Research PDF Watermarker")
    print(f"{'DRY RUN — no files will be changed' if args.dry_run else 'LIVE — originals backed up to _originals/'}")
    print(f"Found {len(pdfs)} PDFs\n")

    ok = 0
    fail = 0
    for pdf in pdfs:
        if watermark_pdf(pdf, dry_run=args.dry_run):
            ok += 1
        else:
            fail += 1

    print(f"\nDone: {ok} stamped, {fail} skipped")

    # Cleanup temp seal
    if _seal_jpg_path and os.path.exists(_seal_jpg_path):
        os.unlink(_seal_jpg_path)


if __name__ == "__main__":
    main()
