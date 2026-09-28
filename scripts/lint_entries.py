#!/usr/bin/env python3
"""Read-only lint for design-style-atlas style entries.

Checks:
- non-placeholder entries have YAML frontmatter + 8 section headings
- criterion and anti-pattern sentences are unique across entries
- (merged 2026-09-28) "## §9 例外通道" allowed only when exception: true; §1–§8 still required
- (merged 2026-09-28) §1/§2 items may be numbered ("1. ...") or ID bullets ("- IT-1 ...", "- AC-AP-1 ...")
- (merged 2026-09-28) §6 decisions: 5 tool keys; midjourney no "--style raw";
  seedream uses art_style (art_style_first rejected); dalle3 carries deprecated: "2026-05-12"
- (merged 2026-09-28) no Pantone chip numbers such as "Pantone 186 C"
Usage: python3 scripts/lint_entries.py [ROOT]   (ROOT defaults to the repo root)
Exit 0 on pass, 1 on fail.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
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
SEC9 = "## §9 例外通道"
BOUNDARIES = REQUIRED_HEADINGS + [SEC9]
TOOL_KEYS = ["midjourney:", "stable_diffusion:", "seedream:", "dalle3:", "flux:"]
PANTONE_CHIP = re.compile(r"(?i)\b(?:pantone|pms)\s+\d{2,4}\s?[cu]\b")
ITEM = re.compile(r"\s*(?:\d+\.|[-*]\s+[A-Z]{2,}(?:-[A-Z]+)*-\d+)\s+(.*)$")


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
        m = ITEM.match(line)
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
        is_exc = meta.get("exception", "").split("#")[0].strip().lower() == "true"
        if re.search(r"^## §9", body, re.M):
            if not is_exc:
                errors.append(f"{path.name}: §9 present but exception is not true")
            elif SEC9 not in body:
                errors.append(f"{path.name}: §9 heading must be '{SEC9}'")
        elif is_exc:
            errors.append(f"{path.name}: exception: true should carry '{SEC9}'")
        s6 = section_body(body, "## §6 提示词出口", BOUNDARIES)
        for k in TOOL_KEYS:
            if k not in s6:
                errors.append(f"{path.name}: §6 missing tool key {k}")
        if "--style raw" in s6:
            errors.append(f"{path.name}: §6 uses '--style raw' (decision: --raw)")
        if "art_style_first" in s6:
            errors.append(f"{path.name}: §6 uses art_style_first (decision: art_style)")
        if not re.search(r"seedream:\s*\{\s*art_style:", s6):
            errors.append(f"{path.name}: §6 seedream must use art_style")
        if not re.search(r"dalle3:.*deprecated:\s*\"?2026-05-12", s6):
            errors.append(f"{path.name}: §6 dalle3 must carry deprecated: 2026-05-12")
        if PANTONE_CHIP.search(text):
            errors.append(f"{path.name}: Pantone chip number found")
        c_list = numbered_sentences(section_body(body, "## §1 判据", BOUNDARIES))
        a_list = numbered_sentences(section_body(body, "## §2 反模式", BOUNDARIES))
        if len(c_list) < 3:
            errors.append(f"{path.name}: §1 needs ≥3 numbered criteria (got {len(c_list)})")
        if len(a_list) < 3:
            errors.append(f"{path.name}: §2 needs ≥3 numbered anti-patterns (got {len(a_list)})")
        if "## §8 区分度自检" in body:
            s8 = section_body(body, "## §8 区分度自检", BOUNDARIES).strip()
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
