#!/usr/bin/env python3
"""Build and register catalogues for dead/classical and fictional/conlang languages."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ROOT / "locales"
META = ROOT / "locales.json"

# 1. Classical Latin (la) - 🏛️
LATIN = {
    "Cancel": "Abrogare", "Save": "Servare", "Delete": "Delere", "Edit": "Recensere",
    "Download": "Depromere", "Close": "Claudere", "Copy": "Exscribere", "Remove": "Removere",
    "Name": "Nomen", "Pause": "Intermittere", "Loading…": "Oneratur…", "Keep": "Retinere",
    "Resume": "Continuare", "Dismiss": "Dimittere", "Unpin": "Defigere", "Add": "Addere",
    "Stop": "Sistere", "Title": "Titulus", "Open": "Aperire", "Preview": "Praevidere",
    "Assets": "Bona", "Off": "Exstinctum", "On": "Accensum", "Create": "Creare",
    "Today": "Hodie", "Accept": "Accipere", "Copied": "Exscriptum", "Settings": "Optiones",
    "Clear": "Purgare", "Hide": "Occultare", "Model": "Exemplar", "Agent": "Agens",
    "Agents": "Agentes", "Prompt": "Incitatio", "System prompt": "Incitatio systematis",
    "Tokens": "Tesserae", "Skip": "Praeterire", "Rename": "Renominare", "Copy link": "Exscribere vinculum",
    "Refresh": "Reficere", "Discard": "Abicere", "Reset": "Redintegrare", "Unfiled": "Non digestum",
    "Collection": "Collectio", "Send": "Mittere", "Generate": "Generare", "Favorites": "Dilecta",
    "Activity": "Actio", "Models": "Exemplaria", "Search": "Quaerere", "Show": "Monstrare",
    "Continue": "Pergere", "Try again": "Iterum conari", "Installed": "Constitutum",
    "Folder": "Scrinium", "Projects": "Incepta", "Username": "Nomen usoris", "Email": "Litterae electronicae",
    "Test": "Probatio", "Discard your changes?": "Visne mutationes abicere?", "Good evening": "Vesper bonum",
    "Library": "Bibliotheca", "Scheduled": "Constitutum", "Yesterday": "Heri", "Never": "Numquam",
    "Recent": "Recentia", "Account": "Ratio", "General": "Generalia", "Appearance": "Aspectus",
    "Shortcuts": "Compendia", "Default agent": "Agens principalis", "Language": "Lingua",
    "Automatic": "Automatica", "Memory": "Memoria", "Speech": "Vox", "API keys": "Claves API",
    "Integrations": "Integrationes", "Usage": "Usus", "Backups": "Copia subsidiaria",
    "About": "De Shell:B", "Log out": "Discedere", "New chat": "Novus sermo", "Search chats": "Quaerere sermones",
    "All": "Omnia", "Chats": "Sermones", "Files": "Fasciculi", "Online sources": "Fontes interretiales",
    "Verified": "Verificatum", "Needs review": "Recognoscendum", "Confirm": "Confirmare"
}

# 2. Ancient Greek (grc) - 🏺
ANCIENT_GREEK = {
    "Cancel": "Ἀκυροῦν", "Save": "Σῴζειν", "Delete": "Διαγράφειν", "Edit": "Διορθοῦν",
    "Download": "Καταβιβάζειν", "Close": "Κλείειν", "Copy": "Ἀντιγράφειν", "Remove": "Ἀφαιρεῖν",
    "Name": "Ὄνομα", "Pause": "Παύειν", "Loading…": "Φορτίζεται…", "Keep": "Φυλάττειν",
    "Resume": "Ἐπαναλαμβάνειν", "Dismiss": "Ἀποπέμπειν", "Unpin": "Ἀποκαθηλοῦν", "Add": "Προστιθέναι",
    "Stop": "Ἵστασθαι", "Title": "Τίτλος", "Open": "Ἀνοίγειν", "Preview": "Προεπισκόπησις",
    "Assets": "Κτήματα", "Off": "Ἀνενεργόν", "On": "Ἐνεργόν", "Create": "Κτίζειν",
    "Today": "Σήμερον", "Accept": "Δέχεσθαι", "Copied": "Ἀντεγράφη", "Settings": "Ῥυθμίσεις",
    "Clear": "Καθαρίζειν", "Hide": "Κρύπτειν", "Model": "Παράδειγμα", "Agent": "Πράκτωρ",
    "Agents": "Πράκτορες", "Prompt": "Παρόρμησις", "System prompt": "Παρόρμησις συστήματος",
    "Tokens": "Σύμβολα", "Skip": "Ὑπερβαίνειν", "Rename": "Μετονομάζειν", "Copy link": "Ἀντιγράφειν σύνδεσμον",
    "Refresh": "Ἀνανεοῦν", "Discard": "Ἀπορρίπτειν", "Reset": "Ἐπαναφέρειν", "Unfiled": "Ἄτακτον",
    "Collection": "Συλλογή", "Send": "Πέμπειν", "Generate": "Γεννᾶν", "Favorites": "Φίλα",
    "Activity": "Ἐνέργεια", "Models": "Παραδείγματα", "Search": "Ζητεῖν", "Show": "Δεικνύναι",
    "Continue": "Συνεχίζειν", "Try again": "Πάλιν πειρᾶσθαι", "Installed": "Ἐγκατεστημένον",
    "Folder": "Φάκελος", "Projects": "Ἔργα", "Username": "Ὄνομα χρήστου", "Email": "Ἠλεκτρονικὴ ἐπιστολή",
    "Test": "Δοκιμή", "Discard your changes?": "Ἀπορρίπτειν τὰς μεταβολάς;", "Good evening": "Χαῖρε ἑσπέρα",
    "Library": "Βιβλιοθήκη", "Scheduled": "Προτεταγμένον", "Yesterday": "Χθές", "Never": "Οὐδέποτε",
    "Recent": "Πρόσφατα", "Account": "Λογαριασμός", "General": "Γενικά", "Appearance": "Ἐμφάνισις",
    "Shortcuts": "Συντομεύσεις", "Default agent": "Προκαθορισμένος πράκτωρ", "Language": "Γλῶσσα",
    "Automatic": "Αὐτόματον", "Memory": "Μνήμη", "Speech": "Φωνή", "API keys": "Κλεῖδες API",
    "Integrations": "Ἑνώσεις", "Usage": "Χρῆσις", "Backups": "Ἀντίγραφα", "About": "Περὶ Shell:B",
    "Log out": "Ἔξοδος", "New chat": "Νέος διάλογος", "Search chats": "Ζητεῖν διαλόγους",
    "All": "Πάντα", "Chats": "Διάλογοι", "Files": "Ἀρχεῖα", "Online sources": "Διαδικτυακαὶ πηγαί",
    "Verified": "Βεβαιωμένον", "Needs review": "Δεῖται ἐλέγχου", "Confirm": "Ἐπιβεβαιοῦν"
}

# 3. Old English / Anglo-Saxon (ang) - 📜
OLD_ENGLISH = {
    "Cancel": "Adilgian", "Save": "Gehealdan", "Delete": "Ofslean", "Edit": "Adihtan",
    "Download": "Niþerhladan", "Close": "Betynean", "Copy": "Geefenlæcan", "Remove": "Afierran",
    "Name": "Nama", "Pause": "Blinnan", "Loading…": "Hladende…", "Keep": "Healdan",
    "Resume": "Ongean settan", "Dismiss": "Forlætan", "Unpin": "Ontigan", "Add": "To-geiecan",
    "Stop": "Gestillan", "Title": "Nama", "Open": "Onsynchron", "Preview": "Foresceawung",
    "Assets": "Æhta", "Off": "Of", "On": "On", "Create": "Sceppan",
    "Today": "Todæg", "Accept": "Onfon", "Copied": "Gecopiod", "Settings": "Gesteallunga",
    "Clear": "Clænsian", "Hide": "Hydan", "Model": "Bysn", "Agent": "Wyrcend",
    "Agents": "Wyrcendas", "Prompt": "Bylding", "System prompt": "Endebyrdnesse bylding",
    "Tokens": "Tacnu", "Skip": "Oferhlapan", "Rename": "Oþernaman", "Copy link": "Geefenlæcan bend",
    "Refresh": "Geedniwian", "Discard": "Aweorpan", "Reset": "Edniwian", "Unfiled": "Ungemet",
    "Collection": "Gadrung", "Send": "Sendan", "Generate": "Acennan", "Favorites": "Leofostan",
    "Activity": "Weorc", "Models": "Bysna", "Search": "Secan", "Show": "Ætiewan",
    "Continue": "Forþgan", "Try again": "Fandian eft", "Installed": "Geseted",
    "Folder": "Fæc", "Projects": "Weorc", "Username": "Brucendnama", "Email": "Ærendgewrit",
    "Test": "Fandung", "Discard your changes?": "Wilt þu aweorpan þine hwearfunga?", "Good evening": "God æfen",
    "Library": "Bochord", "Scheduled": "Geseted", "Yesterday": "Giestran dæge", "Never": "Næfre",
    "Recent": "Niwe", "Account": "Gerim", "General": "Gemæne", "Appearance": "Ansyn",
    "Shortcuts": "Scyrtan wegas", "Default agent": "Forma wyrcend", "Language": "Geþeode",
    "Automatic": "Selflice", "Memory": "Gemynd", "Speech": "Spræc", "API keys": "API cægas",
    "Integrations": "Gefegunga", "Usage": "Brucung", "Backups": "Hordcyste", "About": "Be Shell:B",
    "Log out": "Utgan", "New chat": "Niwe mot", "Search chats": "Secan motas",
    "All": "Eall", "Chats": "Motas", "Files": "Gewritu", "Online sources": "Westerne wellan",
    "Verified": "Gesoþod", "Needs review": "Behealdaþ", "Confirm": "Fæstnian"
}

# 4. Old Norse (non) - ᚱ
OLD_NORSE = {
    "Cancel": "Hætta við", "Save": "Varðveita", "Delete": "Afmá", "Edit": "Bæta",
    "Download": "Hlaða niðr", "Close": "Loka", "Copy": "Rita eftir", "Remove": "Taka burt",
    "Name": "Nafn", "Pause": "Hvíla", "Loading…": "Hleðr…", "Keep": "Halda",
    "Resume": "Halda áfram", "Dismiss": "Vísa frá", "Unpin": "Losa", "Add": "Bæta við",
    "Stop": "Stöðva", "Title": "Titill", "Open": "Opna", "Preview": "Forsýn",
    "Assets": "Góz", "Off": "Af", "On": "Á", "Create": "Skapa",
    "Today": "Í dag", "Accept": "Taka við", "Copied": "Ritað", "Settings": "Stillingar",
    "Clear": "Hreinsa", "Hide": "Fela", "Model": "Líkan", "Agent": "Verkandi",
    "Agents": "Verkendr", "Prompt": "Eggjan", "System prompt": "Eggjan kerfis",
    "Tokens": "Tákn", "Skip": "Stikla", "Rename": "Endurnefna", "Copy link": "Afrita tengil",
    "Refresh": "Endurnýja", "Discard": "Kasta", "Reset": "Endurstilla", "Unfiled": "Óskráð",
    "Collection": "Safn", "Send": "Senda", "Generate": "Geta", "Favorites": "Eftirlæti",
    "Activity": "Iðja", "Models": "Líkön", "Search": "Leita", "Show": "Sýna",
    "Continue": "Halda áfram", "Try again": "Reyna aptr", "Installed": "Sett upp",
    "Folder": "Mappa", "Projects": "Verkefni", "Username": "Notandanafn", "Email": "Póstr",
    "Test": "Raun", "Discard your changes?": "Viltu kasta breytingum?", "Good evening": "Gott kveld",
    "Library": "Bókhlaða", "Scheduled": "Áætlat", "Yesterday": "Í gær", "Never": "Aldri",
    "Recent": "Nýlegt", "Account": "Aðgangr", "General": "Almennt", "Appearance": "Útlit",
    "Shortcuts": "Flýtileiðir", "Default agent": "Sjálfgefinn verkandi", "Language": "Tunga",
    "Automatic": "Sjálfvirkt", "Memory": "Minni", "Speech": "Mál", "API keys": "API lyklar",
    "Integrations": "Samtengingar", "Usage": "Notkun", "Backups": "Öryggisafrit", "About": "Um Shell:B",
    "Log out": "Útskrá", "New chat": "Nýtt spjall", "Search chats": "Leita í spjöllum",
    "All": "Allt", "Chats": "Spjöll", "Files": "Skrár", "Online sources": "Netheimildir",
    "Verified": "Staðfest", "Needs review": "Þarfnast yfirferðar", "Confirm": "Staðfesta"
}

# 5. Esperanto (eo) - 🟢
ESPERANTO = {
    "Cancel": "Nuligi", "Save": "Konservi", "Delete": "Forigi", "Edit": "Redakti",
    "Download": "Elŝuti", "Close": "Fermi", "Copy": "Kopii", "Remove": "Forpreni",
    "Name": "Nomo", "Pause": "Paŭzi", "Loading…": "Ŝargante…", "Keep": "Gardi",
    "Resume": "Daŭrigi", "Dismiss": "Malakcepti", "Unpin": "Malfiksi", "Add": "Aldoni",
    "Stop": "Halti", "Title": "Titolo", "Open": "Malfermi", "Preview": "Antaŭrigardo",
    "Assets": "Rimedoj", "Off": "Malŝaltita", "On": "Ŝaltita", "Create": "Krei",
    "Today": "Hodiaŭ", "Accept": "Akcepti", "Copied": "Kopiita", "Settings": "Agordoj",
    "Clear": "Vakigi", "Hide": "Kaŝi", "Model": "Modelo", "Agent": "Agento",
    "Agents": "Agentoj", "Prompt": "Invito", "System prompt": "Sistema invito",
    "Tokens": "Ĵetonoj", "Skip": "Preterpasi", "Rename": "Renomi", "Copy link": "Kopii ligilon",
    "Refresh": "Reŝargi", "Discard": "Forĵeti", "Reset": "Restarigi", "Unfiled": "Nedosierigita",
    "Collection": "Kolekto", "Send": "Sendi", "Generate": "Generi", "Favorites": "Plej ŝatataj",
    "Activity": "Agado", "Models": "Modeloj", "Search": "Serĉi", "Show": "Montri",
    "Continue": "Daŭrigi", "Try again": "Reprovi", "Installed": "Instalita",
    "Folder": "Dosierujo", "Projects": "Projektoj", "Username": "Uzantnomo", "Email": "Retpoŝto",
    "Test": "Testo", "Discard your changes?": "Ĉu forĵeti viajn ŝanĝojn?", "Good evening": "Bonan vesperon",
    "Library": "Biblioteko", "Scheduled": "Planita", "Yesterday": "Hieraŭ", "Never": "Neniam",
    "Recent": "Freŝaj", "Account": "Konto", "General": "Ĝenerala", "Appearance": "Aspekto",
    "Shortcuts": "Klavkombinoj", "Default agent": "Defaŭlta agento", "Language": "Lingvo",
    "Automatic": "Aŭtomata", "Memory": "Memoro", "Speech": "Voĉo", "API keys": "API-ŝlosiloj",
    "Integrations": "Integriĝoj", "Usage": "Uzo", "Backups": "Savkopioj", "About": "Pri Shell:B",
    "Log out": "Elsaluti", "New chat": "Nova babilado", "Search chats": "Serĉi babiladojn",
    "All": "Ĉiuj", "Chats": "Babiladoj", "Files": "Dosieroj", "Online sources": "Retaj fontoj",
    "Verified": "Verigita", "Needs review": "Revizio bezonata", "Confirm": "Konfirmi"
}

# 6. Klingon (tlh) - ⚔️
KLINGON = {
    "Cancel": "qil", "Save": "pol", "Delete": "teq", "Edit": "choH",
    "Download": "lIS", "Close": "SoQmoH", "Copy": "chenqa'moH", "Remove": "woD",
    "Name": "pong", "Pause": "mev", "Loading…": "lI'taH…", "Keep": "toD",
    "Resume": "taghqa'", "Dismiss": "qI'", "Unpin": "tlhe'", "Add": "chel",
    "Stop": "mev", "Title": "per", "Open": "poSmoH", "Preview": "legh",
    "Assets": "mupwI'mey", "Off": "chu'Ha'", "On": "chu'", "Create": "chenmoH",
    "Today": "DaHjaj", "Accept": "laj", "Copied": "chenqa'moHlu'", "Settings": "choHmey",
    "Clear": "Say'moH", "Hide": "So'", "Model": "mut", "Agent": "toy'wI'",
    "Agents": "toy'wI'pu'", "Prompt": "ra'wI'", "System prompt": "pat ra'wI'",
    "Tokens": "De'mey", "Skip": "taQ", "Rename": "pong chu'", "Copy link": "tlhegh chenqa'",
    "Refresh": "qaDqa'", "Discard": "woD", "Reset": "yuDHa'", "Unfiled": "ngoghHa'",
    "Collection": "bochwI'", "Send": "lab", "Generate": "chen", "Favorites": "bangmey",
    "Activity": "vang", "Models": "mutmey", "Search": "nej", "Show": "cha'",
    "Continue": "taH", "Try again": "nIDqa'", "Installed": "lanlu'",
    "Folder": "teywI'", "Projects": "qughmey", "Username": "pong", "Email": "De'gho",
    "Test": "chov", "Discard your changes?": "choHmeylIj DawoDneH'a'?", "Good evening": "nuqneH ram",
    "Library": "paqvaQ", "Scheduled": "nablu'", "Yesterday": "wa’Hu’", "Never": "not",
    "Recent": "chu'", "Account": "patlh", "General": "Hoch", "Appearance": "leghlu'",
    "Shortcuts": "palthmey", "Default agent": "toy'wI' wa'DIch", "Language": "Hol",
    "Automatic": "e' mam", "Memory": "qawHaq", "Speech": "jatlh", "API keys": "pe'vylmey",
    "Integrations": "mupmey", "Usage": "lo'", "Backups": "polvaQ", "About": "Shell:B potlh",
    "Log out": "mej", "New chat": "ja'chuq chu'", "Search chats": "ja'chuqmey nej",
    "All": "Hoch", "Chats": "ja'chuqmey", "Files": "De'mey", "Online sources": "De'gho 'Internet'",
    "Verified": "toblu'", "Needs review": "nejlu'nIS", "Confirm": "HonHa'"
}

# 7. Sindarin Elvish (sjn) - 🍃
SINDARIN = {
    "Cancel": "Nuitho", "Save": "Bado", "Delete": "Dartha", "Edit": "Taetha",
    "Download": "Toltha", "Close": "Holo", "Copy": "Echono", "Remove": "Hego",
    "Name": "Eneth", "Pause": "Dartha", "Loading…": "Cartha…", "Keep": "Bado",
    "Resume": "Echoro", "Dismiss": "Edra", "Unpin": "Leitho", "Add": "Anno",
    "Stop": "Daro", "Title": "Eneth", "Open": "Edro", "Preview": "Ceno",
    "Assets": "Garn", "Off": "Pel", "On": "Cal", "Create": "Echano",
    "Today": "Sîr", "Accept": "Ganno", "Copied": "Echoniel", "Settings": "Eitiolath",
    "Clear": "Puig", "Hide": "Dolo", "Model": "Cano", "Agent": "Cairon",
    "Agents": "Cairyn", "Prompt": "Horthol", "System prompt": "Horthol e-vroen",
    "Tokens": "Thent", "Skip": "Cab", "Rename": "Eneth edwen", "Copy link": "Echono lîg",
    "Refresh": "Ceuro", "Discard": "Gwenno", "Reset": "Adertho", "Unfiled": "Pen-dôl",
    "Collection": "Gwaith", "Send": "Meno", "Generate": "Onno", "Favorites": "Melethil",
    "Activity": "Caras", "Models": "Cenyr", "Search": "Cesta", "Show": "Tiro",
    "Continue": "Meno", "Try again": "A carno", "Installed": "Orthannen",
    "Folder": "Gwaith", "Projects": "I-ngraith", "Username": "Eneth", "Email": "Têw",
    "Test": "Tyro", "Discard your changes?": "Teithach gwenno?", "Good evening": "Mae thúr",
    "Library": "Gobel", "Scheduled": "Bant", "Yesterday": "Gell", "Never": "U-lû",
    "Recent": "Gwir", "Account": "Gond", "General": "Pân", "Appearance": "Thi",
    "Shortcuts": "Raden", "Default agent": "Cairon min", "Language": "Lam",
    "Automatic": "Silivren", "Memory": "Rîn", "Speech": "Lhaw", "API keys": "Lath",
    "Integrations": "Erthad", "Usage": "I-garn", "Backups": "Bando", "About": "O Shell:B",
    "Log out": "Gwenno", "New chat": "Govannas sein", "Search chats": "Cesta govannath",
    "All": "Pân", "Chats": "Govannath", "Files": "Teithyn", "Online sources": "Eithel lîm",
    "Verified": "Tand", "Needs review": "Baur cenad", "Confirm": "Tanno"
}

# 8. High Valyrian (val) - 🐉
HIGH_VALYRIAN = {
    "Cancel": "Drēje", "Save": "Pāle", "Delete": "Kemze", "Edit": "Rūda",
    "Download": "Mōrī", "Close": "Rupnar", "Copy": "Tympta", "Remove": "Nyke",
    "Name": "Brōzi", "Pause": "Kelmāstis", "Loading…": "Dāerotas…", "Keep": "Pāle",
    "Resume": "Gōvilas", "Dismiss": "Mazilības", "Unpin": "Hūra", "Add": "Olvie",
    "Stop": "Lykirī", "Title": "Brōzi", "Open": "Poenur", "Preview": "Urnēbior",
    "Assets": "Geldio", "Off": "Dāeruni", "On": "Vēzos", "Create": "Kōzō",
    "Today": "Tubio", "Accept": "Rhaenor", "Copied": "Tymptir", "Settings": "Udrir",
    "Clear": "Morghon", "Hide": "Iēdro", "Model": "Perzys", "Agent": "Bantis",
    "Agents": "Bantī", "Prompt": "Ivestretys", "System prompt": "Ivestretys rybno",
    "Tokens": "Gelde", "Skip": "Sōvētē", "Rename": "Kipagon brōzi", "Copy link": "Tympta tegon",
    "Refresh": "Mazōrtys", "Discard": "Nyke", "Reset": "Amāzītis", "Unfiled": "Dāeri",
    "Collection": "Gevie", "Send": "Ivestras", "Generate": "Zōbry", "Favorites": "Keligon",
    "Activity": "Rūs", "Models": "Perzy", "Search": "Jūlor", "Show": "Urnētys",
    "Continue": "Jaelas", "Try again": "Tolvie", "Installed": "Dāerilza",
    "Folder": "Geldio", "Projects": "Valzho", "Username": "Brōzi", "Email": "Tegio",
    "Test": "Zālagon", "Discard your changes?": "Jaelī rūs nykagon?", "Good evening": "Valar morghulis",
    "Library": "Embior", "Scheduled": "Dāeroti", "Yesterday": "Tubī", "Never": "Daor",
    "Recent": "Zōbry", "Account": "Ropun", "General": "Kēli", "Appearance": "Urnēbon",
    "Shortcuts": "Hūren", "Default agent": "Bantis ēlie", "Language": "Engos",
    "Automatic": "Vēzeno", "Memory": "Qilōny", "Speech": "Udrir", "API keys": "Gelde API",
    "Integrations": "Tymptir", "Usage": "Kelis", "Backups": "Pāloti", "About": "Shell:B se",
    "Log out": "Māzigon", "New chat": "Udrir sȳz", "Search chats": "Jūlor udrir",
    "All": "Keli", "Chats": "Udrī", "Files": "Tegī", "Online sources": "Eglie eithel",
    "Verified": "Drēje", "Needs review": "Zālar urnēbon", "Confirm": "Keligon"
}

# 9. Pirate Speak (en-pirate) - 🏴‍☠️
PIRATE = {
    "Cancel": "Belay that!", "Save": "Stash in the chest", "Delete": "Walk the plank!", "Edit": "Scrawl anew",
    "Download": "Haul aboard", "Close": "Batten down", "Copy": "Forge a copy", "Remove": "Cast adrift",
    "Name": "Handle", "Pause": "Drop anchor", "Loading…": "Hoist the sails…", "Keep": "Keep me plunder",
    "Resume": "Set sail again", "Dismiss": "Avast!", "Unpin": "Unfurl pin", "Add": "Stow more",
    "Stop": "Avast ye!", "Title": "Pennant", "Open": "Unfurl!", "Preview": "Spyglass view",
    "Assets": "Booty & plunder", "Off": "Below deck", "On": "On deck", "Create": "Forge anew",
    "Today": "This tide", "Accept": "Aye, agreed!", "Copied": "Copied into me log", "Settings": "Ship's Articles",
    "Clear": "Swab the deck", "Hide": "Stash away", "Model": "Galley mate", "Agent": "First Mate",
    "Agents": "Crew mates", "Prompt": "Captain's Orders", "System prompt": "Admiral's Orders",
    "Tokens": "Doubloons", "Skip": "Skim across", "Rename": "Re-christen", "Copy link": "Copy treasure map",
    "Refresh": "Catch the trade winds", "Discard": "Scuttle it", "Reset": "Back to port", "Unfiled": "Flotsam & jetsam",
    "Collection": "Treasure chest", "Send": "Fire cannons!", "Generate": "Conjure up", "Favorites": "Finest bounty",
    "Activity": "Ship's log", "Models": "Galley mates", "Search": "Scour the seas", "Show": "Spyglass on",
    "Continue": "Carry on sailing", "Try again": "Have another crack", "Installed": "Rigged & ready",
    "Folder": "Sea chest", "Projects": "Expeditions", "Username": "Pirate alias", "Email": "Pigeon dispatch",
    "Test": "Trial run", "Discard your changes?": "Scuttle yer changes overboard?", "Good evening": "Ahoy, dark skies!",
    "Library": "Captain's Archive", "Scheduled": "On the tide table", "Yesterday": "Last sunset", "Never": "Never on seven seas",
    "Recent": "Fresh bounty", "Account": "Quartermaster ledger", "General": "Shipshape", "Appearance": "Rigging & sails",
    "Shortcuts": "Quick ropes", "Default agent": "Right-hand mate", "Language": "Tongue",
    "Automatic": "Follow the sea winds", "Memory": "Crow's nest memories", "Speech": "Chantey & holler", "API keys": "Letter of marque",
    "Integrations": "Allied fleets", "Usage": "Rations & gunpowder", "Backups": "Buried treasure cache", "About": "About Shell:B, arrr!",
    "Log out": "Abandon ship", "New chat": "New yarn", "Search chats": "Search the logs",
    "All": "The whole lot", "Chats": "Yarns", "Files": "Parchments", "Online sources": "Port charts",
    "Verified": "Sturdy & vetted", "Needs review": "Needs the captain's eye", "Confirm": "Aye, aye!"
}

NEW_LOCALES = {
    "la": {
        "name": "Latina", "flag": "🏛️", "category": "dead",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Whitaker's Words", "url": "https://latin-words.com/" },
            { "name": "Perseus Digital Library", "url": "http://www.perseus.tufts.edu/" },
            { "name": "Wiktionary (Latina)", "url": "https://en.wiktionary.org/wiki/Category:Latin_language" }
        ],
        "data": LATIN
    },
    "grc": {
        "name": "Ἑλληνική", "flag": "🏺", "category": "dead",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Perseus Greek Lexicon", "url": "http://www.perseus.tufts.edu/" },
            { "name": "LSJ Greek Dictionary", "url": "https://lsj.gr/" },
            { "name": "Wiktionary (Ἑλληνική)", "url": "https://en.wiktionary.org/wiki/Category:Ancient_Greek_language" }
        ],
        "data": ANCIENT_GREEK
    },
    "ang": {
        "name": "Ænglisc", "flag": "📜", "category": "dead",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Bosworth-Toller Dictionary", "url": "https://bosworthtoller.com/" },
            { "name": "Wiktionary (Old English)", "url": "https://en.wiktionary.org/wiki/Category:Old_English_language" }
        ],
        "data": OLD_ENGLISH
    },
    "non": {
        "name": "Norrœnt mál", "flag": "ᚱ", "category": "dead",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Cleasby-Vigfusson Old Norse", "url": "https://cleasby-vigfusson.ling.upenn.edu/" },
            { "name": "Wiktionary (Old Norse)", "url": "https://en.wiktionary.org/wiki/Category:Old_Norse_language" }
        ],
        "data": OLD_NORSE
    },
    "eo": {
        "name": "Esperanto", "flag": "🟢", "category": "fictional",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Plena Ilustrita Vortaro (PIV)", "url": "https://vortaro.net/" },
            { "name": "Reta Vortaro", "url": "https://reta-vortaro.de/" },
            { "name": "Wiktionary (Esperanto)", "url": "https://en.wiktionary.org/wiki/Category:Esperanto_language" }
        ],
        "data": ESPERANTO
    },
    "tlh": {
        "name": "tlhIngan Hol", "flag": "⚔️", "category": "fictional",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Klingon Language Institute", "url": "https://www.kli.org/" },
            { "name": "Klingon Wiktionary", "url": "https://en.wiktionary.org/wiki/Category:Klingon_language" }
        ],
        "data": KLINGON
    },
    "sjn": {
        "name": "Sindarin", "flag": "🍃", "category": "fictional",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Eldamo Elvish Lexicon", "url": "https://eldamo.org/" },
            { "name": "Parf Edhellen", "url": "https://www.elfdict.com/" },
            { "name": "Wiktionary (Sindarin)", "url": "https://en.wiktionary.org/wiki/Category:Sindarin_language" }
        ],
        "data": SINDARIN
    },
    "val": {
        "name": "Valyrio Eglie", "flag": "🐉", "category": "fictional",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "High Valyrian Dictionary", "url": "https://wiki.languageinvention.com/index.php/High_Valyrian_Dictionary" },
            { "name": "Language Invention Hub", "url": "https://wiki.languageinvention.com/" }
        ],
        "data": HIGH_VALYRIAN
    },
    "en-pirate": {
        "name": "Pirate Speak", "flag": "🏴‍☠️", "category": "fictional",
        "author": "Evie & Shell:B", "authorUrl": "https://github.com/ShellB-App/Shell-B",
        "license": "MIT", "version": "0.1",
        "sources": [
            { "name": "Talk Like A Pirate Glossary", "url": "http://talklikeapirate.com/" },
            { "name": "Pirate English Lexicon", "url": "https://en.wiktionary.org/" }
        ],
        "data": PIRATE
    }
}

FLAGS_FOR_EXISTING = {
    "br": {"flag": "🏴", "category": "living"},
    "cy": {"flag": "🏴󠁧󠁢󠁷󠁬󠁳󠁿", "category": "living"},
    "es": {"flag": "🇪🇸", "category": "living"},
    "eu": {"flag": "🟩", "category": "living"},
    "fr": {"flag": "🇫🇷", "category": "living"},
    "ga": {"flag": "🇮🇪", "category": "living"},
    "gd": {"flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "category": "living"},
    "gv": {"flag": "🇮🇲", "category": "living"},
    "ja": {"flag": "🇯🇵", "category": "living"},
    "kw": {"flag": "⬛", "category": "living"},
    "liv": {"flag": "🇱🇻", "category": "living"},
    "rm": {"flag": "🇨🇭", "category": "living"},
    "smn": {"flag": "🇫🇮", "category": "living"},
    "sr": {"flag": "🇷🇸", "category": "living"},
    "sr-Latn": {"flag": "🇷🇸", "category": "living"},
    "uk": {"flag": "🇺🇦", "category": "living"}
}

def main():
    meta = json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}

    # Update existing with flags and categories
    for code, info in FLAGS_FOR_EXISTING.items():
        if code in meta:
            meta[code]["flag"] = info["flag"]
            meta[code]["category"] = info["category"]

    # Write new catalogues and meta
    for code, entry in NEW_LOCALES.items():
        cat_file = LOCALES / f"{code}.json"
        cat_file.write_text(json.dumps(entry["data"], indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        meta[code] = {
            "name": entry["name"],
            "flag": entry["flag"],
            "category": entry["category"],
            "author": entry["author"],
            "authorUrl": entry["authorUrl"],
            "license": entry["license"],
            "version": entry["version"],
            "sources": entry["sources"]
        }
        print(f"Created catalogue locales/{code}.json with {len(entry['data'])} keys")

    META.write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated locales.json: now has {len(meta)} locales!")

if __name__ == "__main__":
    main()
