#!/usr/bin/env python3
"""Build search-index.json from the reading rows in index.html.

Scans every <div class="row">...</div> on the course page, and for rows
that link to a file mirrored in this repo (badge "pdf" or "html"), extracts
the document's text so the on-page search can match slide/reading content,
not just titles. Rows that only link out to an external/unmirrored source
(badge "ext") are indexed by title/subtitle only — their files, if any
exist locally, are never read.

Run this again after adding or renaming readings:
    python3 tools/build_search_index.py
"""
import html
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = ROOT / "index.html"
OUT_PATH = ROOT / "search-index.json"
MAX_TEXT_CHARS = 20000

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
ROW_RE = re.compile(r'<div class="row( disabled)?">(.*?)</div>')
SECTION_RE = re.compile(r'<section id="([^"]+)">')
H2_RE = re.compile(r"<h2>(.*?)</h2>")
H3_RE = re.compile(r"<h3>(.*?)</h3>")
TITLE_LINK_RE = re.compile(r'<a class="title-link" href="([^"]+)">(.*?)</a>')
SUB_RE = re.compile(r'<span class="sub">(.*?)</span>')
BADGE_RE = re.compile(r'<span class="badge ([a-z]+)">')


def clean_text(s):
    s = SUB_RE.sub(" ", s)  # sub is pulled out separately before this is called
    s = TAG_RE.sub(" ", s)
    s = html.unescape(s)
    return WS_RE.sub(" ", s).strip()


def extract_pdf_text(path):
    try:
        out = subprocess.run(
            ["pdftotext", str(path), "-"],
            capture_output=True, timeout=60,
        )
        return out.stdout.decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ! pdftotext failed for {path}: {e}", file=sys.stderr)
        return ""


def extract_html_text(path):
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  ! read failed for {path}: {e}", file=sys.stderr)
        return ""
    raw = SCRIPT_STYLE_RE.sub(" ", raw)
    raw = TAG_RE.sub(" ", raw)
    raw = html.unescape(raw)
    return raw


def main():
    src = INDEX_HTML.read_text(encoding="utf-8")
    lines = src.splitlines()

    entries = []
    section = ""
    pending_h2 = pending_h3 = None
    in_section = False

    for line in lines:
        if SECTION_RE.search(line):
            in_section = True
            pending_h2 = pending_h3 = None
            continue
        if in_section:
            m = H2_RE.search(line)
            if m:
                pending_h2 = clean_text(m.group(1))
            m = H3_RE.search(line)
            if m:
                pending_h3 = clean_text(m.group(1))
                section = " · ".join(p for p in (pending_h2, pending_h3) if p)

        rm = ROW_RE.search(line)
        if not rm:
            continue
        row_html = rm.group(2)
        tm = TITLE_LINK_RE.search(row_html)
        if not tm:
            continue
        href, inner = tm.group(1), tm.group(2)
        sub_m = SUB_RE.search(inner)
        sub = clean_text(sub_m.group(1)) if sub_m else ""
        title = clean_text(inner)
        badge_m = BADGE_RE.search(row_html)
        badge = badge_m.group(1) if badge_m else ""

        text = ""
        if badge in ("pdf", "html") and not href.startswith("http"):
            rel = urllib.parse.unquote(href)
            fpath = ROOT / rel
            if fpath.exists():
                print(f"indexing [{badge}] {title}")
                raw = extract_pdf_text(fpath) if fpath.suffix.lower() == ".pdf" else extract_html_text(fpath)
                text = WS_RE.sub(" ", raw).strip()[:MAX_TEXT_CHARS]
            else:
                print(f"  ! missing file for row: {fpath}", file=sys.stderr)

        entries.append({
            "title": title,
            "sub": sub,
            "section": section,
            "href": href,
            "type": badge,
            "text": text,
        })

    OUT_PATH.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    total_text = sum(len(e["text"]) for e in entries)
    print(f"\nWrote {len(entries)} entries ({total_text:,} chars of body text) to {OUT_PATH.relative_to(ROOT)}")
    print(f"File size: {OUT_PATH.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
