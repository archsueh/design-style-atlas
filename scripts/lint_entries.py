#!/usr/bin/env python3
"""Read-only lint for design-style-atlas style entries.

Checks:
- non-placeholder entries have YAML frontmatter + 8 section headings
- criterion and anti-pattern sentences are unique across entries
Exit 0 on pass, 1 on fail.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES = ROOT / "styles"
REQUIRED_HEADINGS = [
    "## §1 判据",
    "## §2 反模式",
    "## §3 排版机制",
    "## §4 色彩",
    "## §5 字体",
    "## §6 提示词出口",
    "## §7 来源与既有实现",
    "## §8 区分度自检",
]


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, parts[2]


def numbered_sentences(section: str) -> list[str]:
    out = []
    for line in section.splitlines():
        m = re.match(r"\s*\d+\.\s+(.*)$", line)
        if m:
            s = re.sub(r"\s+", " ", m.group(1)).strip()
            if s:
                out.append(s)
    return out


def section_body(text: str, heading: str, headings: list[str]) -> str:
    idx = text.find(heading)
    if idx < 0:
        return ""
    start = idx + len(heading)
    end = len(text)
    for h in headings:
        if h == heading:
            continue
        j = text.find(h, start)
        if j >= 0:
            end = min(end, j)
    return text[start:end]


def main() -> int:
    errors: list[str] = []
    crit: dict[str, str] = {}
    anti: dict[str, str] = {}
    ready = 0

    for path in sorted(STYLES.glob("*.md")):
        if path.name.startswith("_index"):
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        status = meta.get("status", "")
        if status == "placeholder":
            if any(h in text for h in REQUIRED_HEADINGS):
                errors.append(f"{path.name}: placeholder must not contain schema sections")
            if "待用户补名" not in text:
                errors.append(f"{path.name}: placeholder missing 待用户补名")
            continue
        if status not in {"ready", "draft"}:
            errors.append(f"{path.name}: missing status ready|draft|placeholder")
            continue
        ready += 1
        for h in REQUIRED_HEADINGS:
            if h not in body:
                errors.append(f"{path.name}: missing {h}")
        c_list = numbered_sentences(section_body(body, "## §1 判据", REQUIRED_HEADINGS))
        a_list = numbered_sentences(section_body(body, "## §2 反模式", REQUIRED_HEADINGS))
        if len(c_list) < 3:
            errors.append(f"{path.name}: §1 needs ≥3 numbered criteria (got {len(c_list)})")
        if len(a_list) < 3:
            errors.append(f"{path.name}: §2 needs ≥3 numbered anti-patterns (got {len(a_list)})")
        if "## §8 区分度自检" in body:
            s8 = section_body(body, "## §8 区分度自检", REQUIRED_HEADINGS).strip()
            if len(s8) < 20:
                errors.append(f"{path.name}: §8 too short")
        for s in c_list:
            if s in crit:
                errors.append(f"duplicate criterion: {path.name!r} vs {crit[s]!r}: {s}")
            else:
                crit[s] = path.name
        for s in a_list:
            if s in anti:
                errors.append(f"duplicate anti-pattern: {path.name!r} vs {anti[s]!r}: {s}")
            else:
                anti[s] = path.name

    if ready < 3:
        errors.append(f"expected ≥3 non-placeholder entries, got {ready}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print(f"PASS  ready={ready} unique_criteria={len(crit)} unique_anti={len(anti)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
