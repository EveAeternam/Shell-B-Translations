#!/usr/bin/env python3
"""Verify translation catalogues against online terminology sources and quality rules.

Usage:
    python3 scripts/verify.py --all
    python3 scripts/verify.py --lang gd
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ROOT / "locales"
VERIFICATION = ROOT / "verification"
KEYS_FILE = ROOT / "keys.json"
META_FILE = ROOT / "locales.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sources  # noqa: E402

PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")


def verify_catalogue(code: str) -> dict:
    cat_file = LOCALES / f"{code}.json"
    if not cat_file.exists():
        return {"code": code, "error": "file not found"}

    meta = json.loads(META_FILE.read_text(encoding="utf-8")) if META_FILE.exists() else {}
    lang_info = meta.get(code, {})
    cat = json.loads(cat_file.read_text(encoding="utf-8"))

    established = sources.ESTABLISHED_ROOTS.get(code, {})
    online_sources_list = lang_info.get("sources") or sources.ONLINE_SOURCES.get(code, [])

    # Check already confirmed keys in existing verification file if present
    VERIFICATION.mkdir(parents=True, exist_ok=True)
    ver_file = VERIFICATION / f"{code}.json"
    confirmed_keys = set()
    if ver_file.exists():
        try:
            prev = json.loads(ver_file.read_text(encoding="utf-8"))
            confirmed_keys = set(prev.get("confirmedKeys", []))
        except Exception:
            pass

    verified_count = 0
    needs_review = []

    for k, v in cat.items():
        if not isinstance(v, str) or not v.strip():
            continue

        want_ph = set(PLACEHOLDER_RE.findall(k))
        got_ph = set(PLACEHOLDER_RE.findall(v))
        if want_ph != got_ph:
            lookup = sources.get_online_lookup_url(code, k)
            needs_review.append({
                "key": k,
                "translation": v,
                "confidence": 0.3,
                "reason": f"Placeholder mismatch: expected {want_ph}, found {got_ph}",
                "lookupSource": lookup["name"],
                "lookupUrl": lookup["url"]
            })
            continue

        # Check identical English strings (acceptable only for very short words/brand names)
        if v == k and len(k) > 10 and k not in confirmed_keys:
            lookup = sources.get_online_lookup_url(code, k)
            needs_review.append({
                "key": k,
                "translation": v,
                "confidence": 0.4,
                "reason": "String left identical to English; may need native translation",
                "lookupSource": lookup["name"],
                "lookupUrl": lookup["url"]
            })
            continue

        # Established terminology check (e.g. Agent -> Neach-gnìomha)
        if k in established and established[k].lower() not in v.lower() and k not in confirmed_keys:
            lookup = sources.get_online_lookup_url(code, k)
            needs_review.append({
                "key": k,
                "translation": v,
                "confidence": 0.6,
                "reason": f"Expected established root '{established[k]}' for '{k}'",
                "lookupSource": lookup["name"],
                "lookupUrl": lookup["url"]
            })
            continue

        verified_count += 1

    total = len(cat)
    verified_pct = round(100.0 * verified_count / max(1, total), 1)

    result = {
        "code": code,
        "name": lang_info.get("name", code),
        "total": total,
        "verified": verified_count,
        "verifiedPct": verified_pct,
        "sources": online_sources_list,
        "needsReviewCount": len(needs_review),
        "needsReview": needs_review[:50],  # cap to top 50
        "confirmedKeys": list(confirmed_keys)
    }

    ver_file.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main():
    parser = argparse.ArgumentParser(description="Verify translation catalogues")
    parser.add_argument("--lang", default="all", help="Language code or 'all'")
    parser.add_argument("--all", dest="all_langs", action="store_true", help="Verify all languages")
    args = parser.parse_args()

    meta = json.loads(META_FILE.read_text(encoding="utf-8")) if META_FILE.exists() else {}
    codes = list(meta.keys()) if (args.lang == "all" or args.all_langs) else [args.lang]

    print(f"{'Code':<8} {'Language':<18} {'Total':<8} {'Verified':<10} {'Review Due':<12} {'Online Sources'}")
    print("-" * 75)
    for code in codes:
        res = verify_catalogue(code)
        if "error" in res:
            continue
        src_names = ", ".join(s["name"] for s in res.get("sources", [])[:2])
        print(f"{res['code']:<8} {res['name']:<18} {res['total']:<8} {res['verifiedPct']:<10}% {res['needsReviewCount']:<12} {src_names}")


if __name__ == "__main__":
    main()
