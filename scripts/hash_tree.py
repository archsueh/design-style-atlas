#!/usr/bin/env python3
"""hash_tree.py — systematic diagnostic for E0's `tree_sha256_12` baseline.

Background
----------
E0 (design-style-atlas v2 pre-check) recorded a 12-hex-char sha256 prefix
per style entry as a third-party reproducibility baseline. The exact
hashing procedure was never documented. 16 hand-tried variants failed to
reproduce vignelli's recorded prefix `5eea37ca96a2`.

This script does NOT assume the answer. It enumerates hashing strategies
systematically and reports any that match a set of known target prefixes
(passed via --targets). It is a search tool, meant to make the attempt
reproducible and to surface the winning strategy once found.

Strategy space covered
----------------------
  orderings : git-ls-tree order, name-sorted, name-sorted-reverse, mtime
  content   : full file, frontmatter-only (between first pair of ---),
              body-only, stripped (no trailing newline), whitespace-normalized
  aggregation: concat-all-then-hash,
               hash-each-then-concat-in-order-then-hash,
               hash-each-then-concat-sorted-then-hash
  extras    : with/without file path included, with/without trailing newline
              between concatenated files, with/without directory entries

Usage
-----
  python3 hash_tree.py [repo_root] [--targets targets.txt]
  python3 hash_tree.py /path/to/design-style-atlas --targets known.txt

`targets.txt` is one 12-hex prefix per line (or any hex string to match
as a prefix). If omitted, the script just prints all candidate prefixes
for manual inspection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


def tracked_files(repo: Path) -> list[Path]:
    """Return git-tracked files (excluding .git) in ls-tree order."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "ls-tree", "-r", "--name-only", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        # Fallback: walk the tree, skip .git
        files = [p for p in repo.rglob("*") if p.is_file() and ".git" not in p.parts]
        return sorted(files)
    return [repo / ln for ln in out.splitlines() if ln.strip()]


def orderings(files: list[Path]) -> dict[str, list[Path]]:
    by_name = sorted(files, key=lambda p: str(p))
    res = {
        "git": files,
        "sorted": by_name,
        "sorted_rev": list(reversed(by_name)),
    }
    try:
        res["mtime"] = sorted(files, key=lambda p: p.stat().st_mtime)
    except OSError:
        pass
    return res


def content_modes(raw: bytes) -> dict[str, bytes]:
    modes: dict[str, bytes] = {"full": raw, "frontmatter": b"", "body": b""}
    text = raw.decode("utf-8", "replace")

    # frontmatter-only: between the first pair of `---` lines
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[: end + 4]
            modes["frontmatter"] = fm.encode("utf-8")
            # body-only: after the first closing `---`
            modes["body"] = text[end + 4:].encode("utf-8")

    modes["stripped"] = raw.rstrip(b"\n")
    # whitespace-normalized
    norm = "\n".join(" ".join(ln.split()) for ln in text.splitlines())
    modes["normalized"] = norm.encode("utf-8")
    return modes


def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", nargs="?", default=".", help="repo root (default: .)")
    ap.add_argument("--targets", help="file of known hex prefixes, one per line")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    targets: list[str] = []
    if args.targets:
        targets = [ln.strip().lower() for ln in Path(args.targets).read_text().splitlines()
                   if ln.strip()]

    files = tracked_files(repo)
    print(f"[hash_tree] repo={repo} files={len(files)}", file=sys.stderr)

    orders = orderings(files)
    matches: list[tuple[str, str, str]] = []  # (strategy, prefix, file_count)

    for oname, ofiles in orders.items():
        # Precompute content modes per file
        per_file: list[dict[str, bytes]] = []
        for f in ofiles:
            try:
                raw = f.read_bytes()
            except OSError:
                raw = b""
            per_file.append(content_modes(raw))

        for cname, _ in [("full", 0), ("frontmatter", 0), ("body", 0),
                         ("stripped", 0), ("normalized", 0)]:
            for with_path in (False, True):
                for with_newline in (False, True):
                    # ---- aggregation A: concat all then hash ----
                    buf = bytearray()
                    for f, modes in zip(ofiles, per_file):
                        c = modes[cname]
                        if with_path:
                            buf += str(f.relative_to(repo)).encode("utf-8")
                            buf += b"\x00"
                        buf += c
                        if with_newline:
                            buf += b"\n"
                    digest = sha256_hex(bytes(buf))
                    prefix = digest[:12]
                    if any(prefix.startswith(t) or digest.startswith(t) for t in targets):
                        matches.append((f"{oname}/{cname}/path={with_path}/nl={with_newline}/concat", prefix, str(len(ofiles))))
                    elif not targets:
                        print(f"{oname:10} {cname:12} path={with_path!s:5} nl={with_newline!s:5} concat -> {prefix}")

                    # ---- aggregation B: hash-each then concat (in order) ----
                    parts = []
                    for f, modes in zip(ofiles, per_file):
                        c = modes[cname]
                        h = sha256_hex(c)
                        if with_path:
                            h = sha256_hex((str(f.relative_to(repo)) + "\x00" + h).encode("utf-8"))
                        parts.append(h)
                    digest2 = sha256_hex(("\n".join(parts) if with_newline else "".join(parts)).encode("utf-8"))
                    p2 = digest2[:12]
                    if any(p2.startswith(t) or digest2.startswith(t) for t in targets):
                        matches.append((f"{oname}/{cname}/path={with_path}/nl={with_newline}/hashcat", p2, str(len(ofiles))))
                    elif not targets:
                        print(f"{oname:10} {cname:12} path={with_path!s:5} nl={with_newline!s:5} hashcat -> {p2}")

                    # ---- aggregation C: hash-each then concat (sorted) ----
                    parts_sorted = sorted(parts)
                    digest3 = sha256_hex(("\n".join(parts_sorted) if with_newline else "".join(parts_sorted)).encode("utf-8"))
                    p3 = digest3[:12]
                    if any(p3.startswith(t) or digest3.startswith(t) for t in targets):
                        matches.append((f"{oname}/{cname}/path={with_path}/nl={with_newline}/hashcat_sorted", p3, str(len(ofiles))))
                    elif not targets:
                        print(f"{oname:10} {cname:12} path={with_path!s:5} nl={with_newline!s:5} hashcat_sorted -> {p3}")

    if targets:
        print(f"\n[hash_tree] targets={targets}")
        if matches:
            print(f"[hash_tree] MATCHES ({len(matches)}):")
            for strat, prefix, n in matches:
                print(f"  {prefix}  ({n} files)  {strat}")
        else:
            print("[hash_tree] no match found across enumerated strategies.")
            print("[hash_tree] try adding directory-entry strategies or git-tree hashing if still open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
