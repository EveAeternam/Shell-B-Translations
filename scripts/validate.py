#!/usr/bin/env python3
"""Check every catalogue in locales/<code>.json against keys.json and build index.json and the README table.

A catalogue maps Shell:B's English interface strings (the keys) to their translation. keys.json is the list of
strings the interface uses, exported from Shell:B's UI source; a catalogue needs no entry for a string it leaves in
English, so coverage is reported, not required. Placeholders such as {name} must survive translation. Standard
library only; run from the repository root:

    python3 -I scripts/validate.py          # check + rebuild index.json and the README table
    python3 -I scripts/validate.py --check  # check only (CI); exits 1 on any error or stale generated file
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ROOT / "locales"
README = ROOT / "README.md"
KEYS = ROOT / "keys.json"
META = ROOT / "locales.json"
CODE_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z]{2,4})?$")
PLACEHOLDER = re.compile(r"\{(\w+)\}")
START, END = "<!-- locales:start -->", "<!-- locales:end -->"


def _forms(v) -> list[str]:
    """The translation's text forms: one string, or a plural's {one, other, …} / list of forms."""
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        return [x for x in v.values() if isinstance(x, str)]
    return [x for x in v if isinstance(x, str)] if isinstance(v, list) else []


def _form_ok(v) -> bool:
    return isinstance(v, str) or (isinstance(v, (dict, list)) and bool(_forms(v)) and len(_forms(v)) == len(v))


def check(path: Path, keys: set[str], meta: dict) -> tuple[dict | None, list[str], list[str]]:
    errors, warnings = [], []
    code = path.stem
    if not CODE_RE.match(code):
        errors.append(f"file name {code!r}: a BCP 47 code such as fr, pt-BR, zh-Hant")
    try:
        cat = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, [f"not valid JSON: {e}"], []
    if not isinstance(cat, dict) or any(not isinstance(k, str) or not _form_ok(v) for k, v in cat.items()):
        return None, ["the catalogue must be one object: English string → translation (a string, or {one, other} forms for a plural)"], []
    info = meta.get(code) or {}
    for key in ("name", "author", "license"):
        if not info.get(key):
            errors.append(f"locales.json needs {key!r} for {code} (name: the language's own name, e.g. Français)")
    empty = [k for k, v in cat.items() if not "".join(_forms(v)).strip()]
    if empty:
        errors.append(f"{len(empty)} empty translations, e.g. {empty[:3]}")
    for k, v in cat.items():
        want = set(PLACEHOLDER.findall(k)) - {"n"}
        for form in _forms(v):
            if set(PLACEHOLDER.findall(form)) - {"n"} != want:
                errors.append(f"placeholders differ: {k!r} → {form!r}")
    same = [k for k, v in cat.items() if k.strip() and v == k and len(k) > 12]
    if same:
        warnings.append(f"{len(same)} entries are identical to the English (fine for names and codes), e.g. {same[:3]}")
    unknown = sorted(set(cat) - keys)
    if unknown:
        warnings.append(f"{len(unknown)} entries aren't current interface strings (stale after a Shell:B update?), e.g. {unknown[:3]}")
    covered = len(set(cat) & keys)
    return {"code": code, "entries": len(cat), "covered": covered, "coverage": round(100 * covered / max(1, len(keys)), 1),
            "name": info.get("name", code), "author": info.get("author", ""), "authorUrl": info.get("authorUrl", ""),
            "license": info.get("license", ""), "version": info.get("version", "1.0")}, errors, warnings


def table_html(index: list[dict]) -> str:
    rows = []
    for it in index:
        by = html.escape(it["author"])
        if it.get("authorUrl"):
            by = f'<a href="{html.escape(it["authorUrl"], quote=True)}">{by}</a>'
        rows.append(f'<tr><td><a href="locales/{it["code"]}.json"><b>{html.escape(it["name"])}</b></a> <code>{it["code"]}</code></td>'
                    f'<td>{it["coverage"]} % ({it["covered"]} of the strings)</td><td><sub>{by} · {html.escape(it["license"])}</sub></td></tr>')
    return f"{START}\n<table>\n<tr><th>Language</th><th>Coverage</th><th>Credit</th></tr>\n" + "\n".join(rows) + f"\n</table>\n{END}"


def readme_with_table(index: list[dict]) -> str | None:
    text = README.read_text()
    if START not in text or END not in text:
        return None
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return head + table_html(index) + tail


def main() -> int:
    check_only = "--check" in sys.argv
    keys = set(json.loads(KEYS.read_text(encoding="utf-8")))
    try:
        meta = json.loads(META.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        meta = {}
    index, bad, stale = [], 0, []
    for path in sorted(LOCALES.glob("*.json")):
        res, errors, warnings = check(path, keys, meta)
        for w in warnings:
            print(f"  {path.stem}: warning: {w}")
        for e in errors:
            print(f"  {path.stem}: ERROR: {e}")
        if errors or res is None:
            bad += 1
            continue
        index.append(res)
    idx = json.dumps({"format": 1, "kind": "locale", "strings": len(keys), "items": index}, indent=1, ensure_ascii=False) + "\n"
    readme = readme_with_table(index)
    if check_only:
        if not (ROOT / "index.json").exists() or (ROOT / "index.json").read_text() != idx:
            stale.append("index.json")
        if readme is not None and readme != README.read_text():
            stale.append("README.md (table)")
        for s in stale:
            print(f"  stale: {s} (run scripts/validate.py and commit)")
    else:
        (ROOT / "index.json").write_text(idx)
        if readme is not None:
            README.write_text(readme)
    print(f"{len(index)} locale{'s' if len(index) != 1 else ''} ok, {bad} with errors" + (f", {len(stale)} generated file(s) stale" if stale else ""))
    return 1 if bad or stale else 0


if __name__ == "__main__":
    sys.exit(main())
