#!/usr/bin/env python3
"""Online dictionary sources and terminology references for Shell:B translations.

Provides authoritative online dictionary lookups (Wiktionary API and national terminology
databases) for grounding translation runs in attested lemmas and giving users direct verification links.
"""
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_FILE = ROOT / ".cache" / "online_terms.json"

ONLINE_SOURCES = {
    "br": [
        {"name": "TermOfis", "url": "https://www.fr.brezhoneg.bzh/", "search": "https://www.fr.brezhoneg.bzh/36-termofis.htm?terme={q}"},
        {"name": "Geriadur Favereau", "url": "https://geriadur.brezhoneg.bzh/", "search": "https://geriadur.brezhoneg.bzh/"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Breton_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "cy": [
        {"name": "Termau Cymru", "url": "https://termau.cymru/", "search": "https://termau.cymru/search?q={q}"},
        {"name": "Geiriadur Prifysgol Cymru", "url": "https://geiriadur.ac.uk/", "search": "https://geiriadur.ac.uk/?page_id=24&lang=en#search={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Welsh_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "es": [
        {"name": "Real Academia Española", "url": "https://dle.rae.es/", "search": "https://dle.rae.es/{q}"},
        {"name": "Wiktionary", "url": "https://es.wiktionary.org/", "search": "https://es.wiktionary.org/wiki/{q}"},
    ],
    "eu": [
        {"name": "Euskalterm", "url": "https://www.euskadi.eus/euskalterm/", "search": "https://www.euskadi.eus/euskalterm/"},
        {"name": "Elhuyar Hiztegia", "url": "https://hiztegiak.elhuyar.eus/", "search": "https://hiztegiak.elhuyar.eus/eu_es/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Basque_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "fr": [
        {"name": "Académie française", "url": "https://www.dictionnaire-academie.fr/", "search": "https://www.dictionnaire-academie.fr/article/{q}"},
        {"name": "Larousse", "url": "https://www.larousse.fr/", "search": "https://www.larousse.fr/dictionnaires/anglais-francais/{q}"},
        {"name": "Wiktionary", "url": "https://fr.wiktionary.org/", "search": "https://fr.wiktionary.org/wiki/{q}"},
    ],
    "ga": [
        {"name": "Téarma.ie", "url": "https://www.tearma.ie/", "search": "https://www.tearma.ie/q/{q}/"},
        {"name": "Teanglann.ie", "url": "https://www.teanglann.ie/", "search": "https://www.teanglann.ie/en/fgb/{q}"},
        {"name": "Foclóir.ie", "url": "https://www.focloir.ie/", "search": "https://www.focloir.ie/en/dictionary/ei/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Irish_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "gd": [
        {"name": "LearnGaelic", "url": "https://learngaelic.net/dictionary/", "search": "https://learngaelic.net/dictionary/index.jsp?abairt={q}"},
        {"name": "Am Faclair Beag", "url": "https://faclair.com/", "search": "https://faclair.com/index.aspx?Language=en&SearchWord={q}"},
        {"name": "Stòr-dàta Briathrachais", "url": "https://www.gaidhlig.scot/", "search": "https://www.gaidhlig.scot/"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Scottish_Gaelic_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "gv": [
        {"name": "LearnManx / Fockleyr", "url": "https://www.learnmanx.com/", "search": "https://www.learnmanx.com/dictionary/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Manx_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "ja": [
        {"name": "Jisho.org", "url": "https://jisho.org/", "search": "https://jisho.org/search/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Japanese_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "kw": [
        {"name": "Akademi Kernewek", "url": "https://cornishdictionary.org.uk/", "search": "https://cornishdictionary.org.uk/?locale=en#search={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Cornish_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "liv": [
        {"name": "Livonian Institute", "url": "https://www.livones.net/", "search": "https://www.livones.net/li/sonorontoz/?q={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Livonian_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "rm": [
        {"name": "Pledari Grond", "url": "https://www.pledarigrond.ch/", "search": "https://www.pledarigrond.ch/rumantschgrischun/#search={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Romansch_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "smn": [
        {"name": "Neahttadigisánit", "url": "https://sanit.oahpa.no/", "search": "https://sanit.oahpa.no/smn/fin/?q={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Inari_Sami_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "sr": [
        {"name": "Vokabular", "url": "https://www.vokabular.rs/", "search": "https://www.vokabular.rs/?lang=sr&search={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Serbian_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "sr-Latn": [
        {"name": "Vokabular", "url": "https://www.vokabular.rs/", "search": "https://www.vokabular.rs/?lang=sr&search={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Serbian_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "uk": [
        {"name": "R2U Academic Dictionaries", "url": "https://r2u.org.ua/", "search": "https://r2u.org.ua/s?w={q}"},
        {"name": "Gorokh", "url": "https://gorokh.pp.ua/", "search": "https://gorokh.pp.ua/Тлумачення/{q}"},
        {"name": "Wiktionary", "url": "https://uk.wiktionary.org/", "search": "https://uk.wiktionary.org/wiki/{q}"},
    ],
    "la": [
        {"name": "Whitaker's Words", "url": "https://latin-words.com/", "search": "https://latin-words.com/"},
        {"name": "Perseus Digital Library", "url": "http://www.perseus.tufts.edu/", "search": "http://www.perseus.tufts.edu/hopper/resolveform?lookup={q}&lang=la"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Latin_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "grc": [
        {"name": "Perseus Greek Lexicon", "url": "http://www.perseus.tufts.edu/", "search": "http://www.perseus.tufts.edu/hopper/resolveform?lookup={q}&lang=greek"},
        {"name": "LSJ Greek Dictionary", "url": "https://lsj.gr/", "search": "https://lsj.gr/wiki/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Ancient_Greek_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "ang": [
        {"name": "Bosworth-Toller Dictionary", "url": "https://bosworthtoller.com/", "search": "https://bosworthtoller.com/search?q={q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Old_English_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "non": [
        {"name": "Cleasby-Vigfusson Old Norse", "url": "https://cleasby-vigfusson.ling.upenn.edu/", "search": "https://cleasby-vigfusson.ling.upenn.edu/"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Old_Norse_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "eo": [
        {"name": "Plena Ilustrita Vortaro (PIV)", "url": "https://vortaro.net/", "search": "https://vortaro.net/#{q}"},
        {"name": "Reta Vortaro", "url": "https://reta-vortaro.de/", "search": "https://reta-vortaro.de/revo/art/{q}.html"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Esperanto_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "tlh": [
        {"name": "Klingon Language Institute", "url": "https://www.kli.org/", "search": "https://www.kli.org/"},
        {"name": "Klingon Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Klingon_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "sjn": [
        {"name": "Eldamo Elvish Lexicon", "url": "https://eldamo.org/", "search": "https://eldamo.org/content/search/search.html?q={q}"},
        {"name": "Parf Edhellen", "url": "https://www.elfdict.com/", "search": "https://www.elfdict.com/w/{q}"},
        {"name": "Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Sindarin_language", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
    "val": [
        {"name": "High Valyrian Dictionary", "url": "https://wiki.languageinvention.com/index.php/High_Valyrian_Dictionary", "search": "https://wiki.languageinvention.com/index.php/Special:Search?search={q}"},
        {"name": "Language Invention Hub", "url": "https://wiki.languageinvention.com/", "search": "https://wiki.languageinvention.com/index.php/Special:Search?search={q}"},
    ],
    "en-pirate": [
        {"name": "Talk Like A Pirate Glossary", "url": "http://talklikeapirate.com/", "search": "http://talklikeapirate.com/"},
        {"name": "Pirate English Lexicon", "url": "https://en.wiktionary.org/", "search": "https://en.wiktionary.org/wiki/{q}"},
    ],
}

# Established native computing terms established for Celtic & minority languages
ESTABLISHED_ROOTS = {
    "gd": {
        "Agent": "Neach-gnìomha",
        "Prompt": "Brostachadh",
        "Tokens": "Comharran",
        "Save": "Sàbhail",
        "Delete": "Sguab às",
        "Search": "Lorg",
        "Cancel": "Sguir dheth",
        "Settings": "Roghainnean",
        "Download": "Luchdaich a-nuas",
        "Close": "Dùin",
    },
    "ga": {
        "Agent": "Gníomhaire",
        "Prompt": "Leid",
        "Tokens": "Comharthaí",
        "Save": "Sábháil",
        "Delete": "Scrios",
        "Search": "Cuardaigh",
        "Cancel": "Cealaigh",
        "Settings": "Socruithe",
        "Download": "Íoslódáil",
        "Close": "Dún",
    },
    "cy": {
        "Agent": "Gweithredydd",
        "Prompt": "Anogwr",
        "Tokens": "Arwyddion",
        "Save": "Cadw",
        "Delete": "Dileu",
        "Search": "Chwilio",
        "Cancel": "Canslo",
        "Settings": "Gosodiadau",
        "Download": "Lawrlwytho",
        "Close": "Cau",
    },
    "gv": {
        "Agent": "Jantagh",
        "Prompt": "Greinneyder",
        "Tokens": "Cowraghyn",
        "Save": "Sauail",
        "Delete": "Scryss",
        "Search": "Ronsaghey",
        "Cancel": "Scuirr",
        "Settings": "Reighyssyn",
    },
    "kw": {
        "Agent": "Gwehythor",
        "Prompt": "Kentryller",
        "Tokens": "Tokyns",
        "Save": "Gwitha",
        "Delete": "Dilea",
        "Search": "Hwilas",
        "Cancel": "Hedhi",
        "Settings": "Settyansow",
    },
    "br": {
        "Agent": "Oberer",
        "Prompt": "Bountell",
        "Tokens": "Arouezioù",
        "Save": "Enrollañ",
        "Delete": "Dilemel",
        "Search": "Klask",
        "Cancel": "Nullañ",
        "Settings": "Arventennoù",
    },
    "la": {
        "Agent": "Actor",
        "Prompt": "Mandatum",
        "Tokens": "Symbola",
        "Save": "Servare",
        "Delete": "Delere",
        "Search": "Quaerere",
        "Cancel": "Abrogare",
        "Settings": "Optiones",
    },
    "grc": {
        "Agent": "Δράστης",
        "Prompt": "Κέλευσμα",
        "Tokens": "Σύμβολα",
        "Save": "Σῴζειν",
        "Delete": "Διαγράφειν",
        "Search": "Ζητεῖν",
        "Cancel": "Ἀκυροῦν",
        "Settings": "Ῥυθμίσεις",
    },
    "ang": {
        "Agent": "Wyrcend",
        "Prompt": "Bebod",
        "Tokens": "Tacnu",
        "Save": "Gehealdan",
        "Delete": "Adilgian",
        "Search": "Secan",
        "Cancel": "Awendan",
        "Settings": "Gesetnessa",
    },
    "non": {
        "Agent": "Vinnandi",
        "Prompt": "Boð",
        "Tokens": "Teikn",
        "Save": "Geyma",
        "Delete": "Fella",
        "Search": "Leita",
        "Cancel": "Hætta",
        "Settings": "Stillingar",
    },
    "eo": {
        "Agent": "Aganto",
        "Prompt": "Instigo",
        "Tokens": "Ĵetonoj",
        "Save": "Konservi",
        "Delete": "Forigi",
        "Search": "Serĉi",
        "Cancel": "Nuligi",
        "Settings": "Agordoj",
    },
    "tlh": {
        "Agent": "toy'wI'",
        "Prompt": "ra'ghach",
        "Tokens": "Deghmey",
        "Save": "pol",
        "Delete": "Qaw'",
        "Search": "nej",
        "Cancel": "mev",
        "Settings": "choHmey",
    },
    "sjn": {
        "Agent": "Ceredir",
        "Prompt": "Canath",
        "Tokens": "Thengnath",
        "Save": "Heba",
        "Delete": "Dartha",
        "Search": "Cesta",
        "Cancel": "Bav",
        "Settings": "Seidhed",
    },
    "val": {
        "Agent": "Konir",
        "Prompt": "Daorilys",
        "Tokens": "Gevessis",
        "Save": "Heptas",
        "Delete": "Nungos",
        "Search": "Jaos",
        "Cancel": "Kelitas",
        "Settings": "Lentun",
    },
    "en-pirate": {
        "Agent": "Deckhand",
        "Prompt": "Order",
        "Tokens": "Doubloons",
        "Save": "Stow",
        "Delete": "Scuttle",
        "Search": "Scout",
        "Cancel": "Belay",
        "Settings": "Ship Riggin'",
    },
}


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_cache(cache: dict):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        CACHE_FILE.write_text(json.dumps(cache, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception:
        pass


_MEM_CACHE = _load_cache()


def get_online_lookup_url(lang_code: str, query: str) -> dict:
    """Return primary online source and direct lookup URL for a term."""
    q_enc = urllib.parse.quote(query.strip())
    sources = ONLINE_SOURCES.get(lang_code, [])
    if not sources:
        return {"name": "Wiktionary", "url": f"https://en.wiktionary.org/wiki/{q_enc}"}
    primary = sources[0]
    return {
        "name": primary["name"],
        "url": primary["search"].format(q=q_enc) if "{q}" in primary.get("search", "") else primary["url"]
    }


def lookup_wiktionary_translations(word: str, lang_code: str) -> list[str]:
    """Query Wiktionary API for attested translations of an English word."""
    clean = re.sub(r"\{[^}]+\}|[^\w\s]", "", word).strip().lower()
    if not clean or len(clean.split()) > 2:
        return []
    target = clean.split()[0]
    cache_key = f"{target}:{lang_code}"
    if cache_key in _MEM_CACHE:
        return _MEM_CACHE[cache_key]

    url = f"https://en.wiktionary.org/w/api.php?action=parse&page={urllib.parse.quote(target)}&prop=wikitext&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "ShellB-Localizer/1.0 (https://github.com/ShellB-App/Shell-B)"})
    matches = []
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            wikitext = data.get("parse", {}).get("wikitext", {}).get("*", "")
            found = re.findall(rf"\{{\{{t\+?\|{lang_code}\|([^|}}]+)", wikitext)
            # Deduplicate preserving order
            matches = list(dict.fromkeys(found))[:4]
    except Exception:
        matches = []

    _MEM_CACHE[cache_key] = matches
    _save_cache(_MEM_CACHE)
    return matches


def build_terminology_reference(keys: list[str], lang_code: str) -> str:
    """Build a grounded reference section of official / online terms for LLM prompting."""
    references = []
    roots = ESTABLISHED_ROOTS.get(lang_code, {})
    for k, v in roots.items():
        references.append(f'- Standard {k}: "{v}"')

    # Look up keywords in keys
    looked_up = set()
    for key in keys:
        clean = re.sub(r"\{[^}]+\}|[^\w\s]", "", key).strip()
        words = clean.split()
        for w in words[:2]:
            w_lower = w.lower()
            if len(w_lower) >= 3 and w_lower not in looked_up and w_lower not in roots:
                looked_up.add(w_lower)
                attested = lookup_wiktionary_translations(w_lower, lang_code)
                if attested:
                    references.append(f'- Online source (Wiktionary) "{w}": {", ".join(attested)}')

    if not references:
        return ""

    return "## Verified Online Terminology References (Official banks & Wiktionary):\n" + "\n".join(references[:15])
