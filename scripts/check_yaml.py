#!/usr/bin/env python3
"""Parse every frontmatter block and every ```yaml fenced block under ROOT/**/*.md.

- If PyYAML is importable, uses yaml.safe_load (authoritative).
- Otherwise falls back to a strict built-in parser for the YAML subset used in
  this repo (block mappings/sequences, flow [..] / {..}, quoted and plain
  scalars, comments). The fallback rejects anything outside that subset, so a
  PASS there is weaker than safe_load; run again where PyYAML exists.
Usage: python3 scripts/check_yaml.py [ROOT]
"""
import glob, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
try:
    import yaml  # type: ignore
    ENGINE = "yaml.safe_load"
except Exception:
    yaml = None
    ENGINE = "builtin-subset"

class E(Exception):
    pass

IND = set('[]{},#&*!|>\'"%@`')

def strip_comment(s):
    q = None; i = 0
    while i < len(s):
        c = s[i]
        if q:
            if q == '"' and c == '\\': i += 2; continue
            if c == q: q = None
        elif c in '"\'' and (i == 0 or s[i-1] in ' [{,:'):
            q = c
        elif c == '#' and (i == 0 or s[i-1] in ' \t'):
            return s[:i].rstrip()
        i += 1
    if q: raise E("unterminated quote")
    return s.rstrip()

def p_quoted(s, i):
    q = s[i]; i += 1; out = []
    while i < len(s):
        c = s[i]
        if q == '"' and c == '\\':
            if i + 1 >= len(s): raise E("bad escape")
            out.append(s[i+1]); i += 2; continue
        if c == q:
            if q == "'" and i + 1 < len(s) and s[i+1] == "'": out.append("'"); i += 2; continue
            return ''.join(out), i + 1
        out.append(c); i += 1
    raise E("unterminated quoted scalar")

def ws(s, i):
    while i < len(s) and s[i] == ' ': i += 1
    return i

def p_flow(s, i):
    i = ws(s, i)
    if i >= len(s): raise E("unexpected end in flow")
    c = s[i]
    if c in '"\'': return p_quoted(s, i)
    if c == '[':
        i += 1; out = []
        i = ws(s, i)
        if i < len(s) and s[i] == ']': return out, i + 1
        while True:
            v, i = p_flow(s, i); out.append(v); i = ws(s, i)
            if i < len(s) and s[i] == ',': i += 1; continue
            if i < len(s) and s[i] == ']': return out, i + 1
            raise E(f"expected , or ] at col {i}")
    if c == '{':
        i += 1; out = {}
        i = ws(s, i)
        if i < len(s) and s[i] == '}': return out, i + 1
        while True:
            i = ws(s, i)
            if s[i] in '"\'': k, i = p_quoted(s, i)
            else:
                m = re.match(r'[^,\[\]{}:#]+', s[i:])
                if not m: raise E(f"bad flow key at col {i}")
                k = m.group(0).strip(); i += m.end()
            if i >= len(s) or s[i] != ':' or (i + 1 < len(s) and s[i+1] not in ' ,}'): raise E(f"expected ': ' after flow key {k!r}")
            i += 1
            v, i = p_flow(s, i); out[k] = v; i = ws(s, i)
            if i < len(s) and s[i] == ',': i += 1; continue
            if i < len(s) and s[i] == '}': return out, i + 1
            raise E(f"expected , or }} at col {i}")
    if c in IND: raise E(f"unexpected indicator {c!r} in flow")
    m = re.match(r'(?:[^,\[\]{}:]|:(?! |,|\}|\]|$))+', s[i:])
    if not m: raise E(f"bad flow scalar at col {i}")
    return m.group(0).strip(), i + m.end()

def p_value(v):
    v = v.strip()
    if v == '': return None
    if v[0] in '[{"\'':
        val, j = p_flow(v, 0)
        if v[j:].strip(): raise E(f"trailing content after value: {v[j:].strip()[:30]!r}")
        return val
    if v[0] in IND or v.startswith('- ') or v.startswith('? '): raise E(f"value starts with indicator: {v[:20]!r}")
    if ': ' in v: raise E(f"plain scalar contains ': ': {v[:30]!r}")
    return v

def p_block(lines, idx, indent):
    first = lines[idx][1]
    if first.startswith('- ') or first == '-':
        out = []
        while idx < len(lines) and lines[idx][0] == indent and (lines[idx][1].startswith('- ') or lines[idx][1] == '-'):
            rest = lines[idx][1][2:]
            if ': ' in rest or rest.endswith(':'): raise E("mapping inside sequence item not supported by fallback")
            out.append(p_value(rest)); idx += 1
        return out, idx
    out = {}
    while idx < len(lines) and lines[idx][0] == indent:
        ln, s = lines[idx][2], lines[idx][1]
        if s[0] in '"\'':
            k, j = p_quoted(s, 0); rest = s[j:]
            if not (rest.startswith(': ') or rest == ':'): raise E(f"line {ln}: expected ': ' after quoted key")
            rest = rest[1:]
        else:
            m = re.match(r'([^\s#\[\]{},:"\'][^:]*?|[^\s#\[\]{},:"\']):( |$)', s)
            if not m: raise E(f"line {ln}: not a 'key: value' line: {s[:40]!r}")
            k = m.group(1); rest = s[m.end(1)+1:]
            if re.search(r'[\[\]{}]', k): raise E(f"line {ln}: flow indicator in key {k!r}")
        if k in out: raise E(f"line {ln}: duplicate key {k!r}")
        try:
            v = p_value(rest)
        except E as e:
            raise E(f"line {ln}: {e}")
        idx += 1
        if v is None and idx < len(lines) and lines[idx][0] > indent:
            v, idx = p_block(lines, idx, lines[idx][0])
        out[k] = v
    if idx < len(lines) and lines[idx][0] > indent:
        raise E(f"line {lines[idx][2]}: bad indentation")
    return out, idx

def builtin_load(text):
    lines = []
    for n, raw in enumerate(text.splitlines(), 1):
        if '\t' in raw[:len(raw) - len(raw.lstrip())]: raise E(f"line {n}: tab indentation")
        if raw.strip() in ('---', '...'): raise E(f"line {n}: document marker '{raw.strip()}' (multi-document)")
        s = strip_comment(raw)
        if not s.strip(): continue
        lines.append((len(s) - len(s.lstrip(' ')), s.strip(), n))
    if not lines: return None
    v, idx = p_block(lines, 0, lines[0][0])
    if idx != len(lines): raise E(f"line {lines[idx][2]}: dedent below root")
    return v

def load(text):
    return yaml.safe_load(text) if yaml else builtin_load(text)

def blocks(root):
    for p in sorted(glob.glob(str(root) + '/**/*.md', recursive=True)):
        t = open(p, encoding='utf-8').read()
        if t.startswith('---\n'):
            j = t.find('\n---', 4)
            yield p, 'frontmatter', t[4:j+1]
        for m in re.finditer(r'^```ya?ml\n(.*?)^```', t, re.S | re.M):
            yield p, 'yaml@L%d' % (t[:m.start()].count('\n') + 1), m.group(1)

def main():
    n = bad = 0
    for p, kind, text in blocks(ROOT):
        n += 1
        try:
            load(text)
        except Exception as e:
            bad += 1
            print(f"FAIL {Path(p).relative_to(ROOT)} {kind}: {str(e).splitlines()[0]}")
    print(f"engine={ENGINE} blocks={n} failed={bad}")
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
