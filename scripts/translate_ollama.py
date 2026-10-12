#!/usr/bin/env python3
"""Batch-translate Shell:B interface strings from keys.json using local Ollama models.

Usage:
    python3 scripts/translate_ollama.py --lang es --limit 50
    python3 scripts/translate_ollama.py --lang all --batch 20
    python3 scripts/translate_ollama.py --sync-sr-latn
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ROOT / "locales"
KEYS_FILE = ROOT / "keys.json"
META_FILE = ROOT / "locales.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sources  # noqa: E402
import verify  # noqa: E402

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "qwen3.6:35b-a3b-q8_0"

LANG_NAMES = {
    # Prioritized endangered and minority languages
    "gd": "Scottish Gaelic (Gàidhlig - native Celtic terminology: Neach-gnìomha for Agent, Brostachadh for Prompt, Comharran for Tokens)",
    "ga": "Irish (Gaeilge - native Celtic terminology: Gníomhaire for Agent, Leid for Prompt, Comharthaí for Tokens)",
    "cy": "Welsh (Cymraeg - native Celtic terminology: Gweithredydd for Agent, Anogwr for Prompt, Arwyddion for Tokens)",
    "gv": "Manx Gaelic (Gaelg - Isle of Man Celtic)",
    "kw": "Cornish (Kernewek - Brythonic Celtic)",
    "br": "Breton (Brezhoneg - Brythonic Celtic)",
    "eu": "Basque (Euskara - Basque isolate)",
    "rm": "Romansh (Rumantsch - Rhaeto-Romance)",
    "liv": "Livonian (Līvõ kēļ - critically endangered Finnic)",
    "smn": "Inari Sami (Anarâškielâ - Sámi)",
    # Other languages
    "es": "Spanish",
    "ja": "Japanese",
    "uk": "Ukrainian",
    "sr": "Serbian (in Serbian Cyrillic script)",
}

PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")

CYR_TO_LAT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E', 'Ж': 'Ž', 'З': 'Z', 'И': 'I',
    'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj', 'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Џ': 'Dž', 'Ш': 'Š',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e', 'ж': 'ž', 'з': 'z', 'и': 'i',
    'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'џ': 'dž', 'ш': 'š'
}


def transliterate_sr_to_latn(val):
    if isinstance(val, str):
        parts = re.split(r'(\{[^}]+\})', val)
        return ''.join(p if (p.startswith('{') and p.endswith('}')) else ''.join(CYR_TO_LAT.get(c, c) for c in p) for p in parts)
    if isinstance(val, dict):
        return {k: transliterate_sr_to_latn(v) for k, v in val.items()}
    if isinstance(val, list):
        return [transliterate_sr_to_latn(v) for v in val]
    return val


def sync_sr_latn():
    sr_file = LOCALES / "sr.json"
    latn_file = LOCALES / "sr-Latn.json"
    if not sr_file.exists():
        print("locales/sr.json not found; skipping sr-Latn sync.")
        return
    sr_data = json.loads(sr_file.read_text(encoding="utf-8"))
    latn_data = {k: transliterate_sr_to_latn(v) for k, v in sr_data.items()}
    latn_file.write_text(json.dumps(latn_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Synced {len(latn_data)} entries to locales/sr-Latn.json from sr.json")


def call_ollama(model: str, messages: list[dict], timeout: int = 180) -> str:
    body = {
        "model": model,
        "messages": messages,
        "format": "json",
        "stream": False,
        "options": {"temperature": 0.1}
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["message"]["content"]


def translate_chunk(keys: list[str], target_lang: str, lang_code: str, model: str) -> dict[str, str]:
    online_refs = sources.build_terminology_reference(keys, lang_code)
    prompt = (
        f"You are a professional software localizer for Shell:B (a clean, modern, private AI workspace).\n"
        f"Translate the following English interface strings into {target_lang}.\n"
        f"Tone: short, direct, natural, no corporate fluff, standard software UI terminology.\n"
        f"Rules:\n"
        f"1. Keep all placeholders like {{name}}, {{v0}}, {{idle}}, {{count}}, etc. exactly as they appear.\n"
        f"2. Return ONLY a valid JSON object mapping the exact original English string to its translation.\n"
        f"3. Do not include extra comments or wrap with markdown code blocks.\n"
    )
    if online_refs:
        prompt += f"\n{online_refs}\nPrioritize terms from these verified online and established references when relevant.\n"
    prompt += f"\nStrings:\n{json.dumps(keys, ensure_ascii=False)}"
    res_str = call_ollama(model, [{"role": "user", "content": prompt}])
    try:
        parsed = json.loads(res_str)
        if isinstance(parsed, dict):
            # Clean and validate keys
            valid = {}
            for k, v in parsed.items():
                if k in keys and isinstance(v, str) and v.strip():
                    want = set(PLACEHOLDER_RE.findall(k))
                    got = set(PLACEHOLDER_RE.findall(v))
                    if want == got:
                        valid[k] = v.strip()
            return valid
    except Exception as e:
        print(f"Failed to parse model response: {e}")
    return {}


def process_language(lang_code: str, model: str, batch_size: int, limit: int | None):
    if lang_code == "sr-Latn":
        sync_sr_latn()
        return

    target_lang = LANG_NAMES.get(lang_code)
    if not target_lang:
        print(f"Unknown language code: {lang_code}")
        return

    cat_file = LOCALES / f"{lang_code}.json"
    catalog = {}
    if cat_file.exists():
        try:
            catalog = json.loads(cat_file.read_text(encoding="utf-8"))
        except Exception:
            catalog = {}

    all_keys = json.loads(KEYS_FILE.read_text(encoding="utf-8"))
    untranslated = [k for k in all_keys if k not in catalog]
    print(f"[{lang_code}] Current coverage: {len(catalog)}/{len(all_keys)}. Remaining: {len(untranslated)}")

    if not untranslated:
        print(f"[{lang_code}] Already 100% complete!")
        return

    to_process = untranslated if limit is None else untranslated[:limit]
    total_added = 0

    for i in range(0, len(to_process), batch_size):
        chunk = to_process[i:i + batch_size]
        print(f"[{lang_code}] Translating batch {i // batch_size + 1} ({len(chunk)} strings)...", end="", flush=True)
        t0 = time.time()
        try:
            results = translate_chunk(chunk, target_lang, lang_code, model)
            catalog.update(results)
            cat_file.write_text(json.dumps(catalog, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            dt = time.time() - t0
            print(f" done in {dt:.1f}s ({len(results)}/{len(chunk)} translated)")
            total_added += len(results)
        except Exception as e:
            print(f" error: {e}")
            break

    print(f"[{lang_code}] Finished run. Added {total_added} translations. Total now: {len(catalog)}")
    try:
        ver = verify.verify_catalogue(lang_code)
        print(f"[{lang_code}] Verification: {ver['verified']}/{ver['total']} verified ({ver['verifiedPct']}%), {ver['needsReviewCount']} pending review.")
    except Exception as e:
        print(f"[{lang_code}] Verification notice: {e}")
    if lang_code == "sr":
        sync_sr_latn()


def main():
    parser = argparse.ArgumentParser(description="Translate Shell:B interface strings with local LLM")
    parser.add_argument("--lang", default="all", help="Language code (es, ja, uk, sr, ga, gd, cy, sr-Latn, all)")
    parser.add_argument("--batch", type=int, default=20, help="Batch size per LLM request")
    parser.add_argument("--limit", type=int, default=None, help="Max strings to translate this run")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama model name")
    parser.add_argument("--sync-sr-latn", action="store_true", help="Sync sr-Latn from sr.json and exit")
    parser.add_argument("--verify", action="store_true", help="Run verification across target languages and exit")
    args = parser.parse_args()

    if getattr(args, "sync_sr_latn", False):
        sync_sr_latn()
        return

    if getattr(args, "verify", False):
        langs = list(LANG_NAMES.keys()) if args.lang == "all" else [args.lang]
        for lang in langs:
            verify.verify_catalogue(lang)
        return

    langs = list(LANG_NAMES.keys()) if args.lang == "all" else [args.lang]
    for lang in langs:
        process_language(lang, args.model, args.batch, args.limit)

    if "sr" in langs or args.lang == "all":
        sync_sr_latn()


if __name__ == "__main__":
    main()
