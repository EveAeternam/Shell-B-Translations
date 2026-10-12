#!/usr/bin/env python3
"""Build and update catalogues for endangered Celtic and European languages."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ROOT / "locales"

# Update existing Celtic catalogues with user-selected terminology
def update_celtic():
    # GD
    gd_file = LOCALES / "gd.json"
    if gd_file.exists():
        gd = json.loads(gd_file.read_text(encoding="utf-8"))
        gd["Agent"] = "Neach-gnìomha"
        gd["Agents"] = "Luchd-gnìomha"
        gd["Prompt"] = "Brostachadh"
        gd["System prompt"] = "Brostachadh an t-siostaim"
        gd["Tokens"] = "Comharran"
        gd_file.write_text(json.dumps(gd, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Updated gd.json with native Celtic roots")

    # GA
    ga_file = LOCALES / "ga.json"
    if ga_file.exists():
        ga = json.loads(ga_file.read_text(encoding="utf-8"))
        ga["Agent"] = "Gníomhaire"
        ga["Agents"] = "Gníomhairí"
        ga["Prompt"] = "Leid"
        ga["System prompt"] = "Leid an chórais"
        ga["Tokens"] = "Comharthaí"
        ga_file.write_text(json.dumps(ga, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Updated ga.json with native Celtic roots")

    # CY
    cy_file = LOCALES / "cy.json"
    if cy_file.exists():
        cy = json.loads(cy_file.read_text(encoding="utf-8"))
        cy["Agent"] = "Gweithredydd"
        cy["Agents"] = "Gweithredyddion"
        cy["Prompt"] = "Anogwr"
        cy["System prompt"] = "Anogwr y system"
        cy["Tokens"] = "Arwyddion"
        cy_file.write_text(json.dumps(cy, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Updated cy.json with native Celtic roots")

GV = {
    "Cancel": "Scuir", "Save": "Sauail", "Delete": "Scryss", "Edit": "Reagh",
    "Download": "Laad neese", "Close": "Doon", "Copy": "Coip", "Remove": "Gow ersooyl",
    "Name": "Ennym", "Pause": "Scur", "Loading…": "Laadey…", "Keep": "Freill",
    "Resume": "Gow toshiaght reesht", "Dismiss": "Cur seose", "Unpin": "Neopinnee", "Add": "Cur lesh",
    "Stop": "Stad", "Title": "Ennym", "Open": "Foshil", "Preview": "Roie-haishbynys",
    "Assets": "Stoyr", "Off": "Ass", "On": "Er", "Create": "Kroo",
    "Today": "Jiu", "Accept": "Soie jannoo", "Copied": "Coipit", "Settings": "Reaghyssyn",
    "Clear": "Glan", "Hide": "Follagh", "Model": "Moyll", "Agent": "Jantagh",
    "Skip": "Lheimm thie", "Rename": "Aan-enmys", "Copy link": "Coip kiangley",
    "Refresh": "Aanoaee", "Discard": "Tilg ersooyl", "Reset": "Aahoshee",
    "Unfiled": "Gyn coad", "Collection": "Çhaglym", "Send": "Cur",
    "Generate": "Genneraghey", "Favorites": "Reihyssyn", "Activity": "Jannoo",
    "Models": "Moyllyn", "Search": "Ronsaghey", "Show": "Taishbyney", "Continue": "Immee er",
    "Try again": "Prow reesht", "Installed": "Shassoo", "Folder": "Foldeyr",
    "Projects": "Shaleeghyn", "Username": "Ennym ymmydeyr", "Email": "Post-l",
    "Test": "Prowaltys", "Discard your changes?": "Tilgey ny caghlaaghyn ayd ersooyl?", "Good evening": "Fastyr mie",
    "Library": "Lioarlan", "Scheduled": "Claarit", "Notes": "Noteyn", "Contacts": "Eishtyn",
    "Toggle theme": "Caghlaa coamrey", "Sign out": "Faill magh", "Sign in": "Faill stiagh",
    "Log in": "Loggal stiagh", "this device": "y saase shoh", "Turn off": "Moogh",
    "Done": "Jeant", "Back": "Ergooyl", "Next": "Yn chied nane elley", "Password": "Fockle arrey",
    "Description": "Coonteys", "None": "Veg", "Mark all read": "Marcail ooilley lhaiht",
    "Undo": "Neoyannoo", "Mark done": "Marcail jeant", "Chat": "Resooney",
    "Messages": "Çhaghteraghtyn", "New project": "Shalee noa", "Pinned": "Pinneyt",
    "Queued": "Ayns straih", "Size": "Mooadys", "Check now": "Jeeagh nish",
    "Delete from disk": "Scryss veih'n jysk", "Used": "Ymmydit", "Stop sharing": "Scuir rheynn",
    "Message": "Çhaghteraght", "Nothing matches.": "Cha nel veg cochormey.", "Memory": "Cooinaghtyn",
    "Tools": "Greienyn", "Usage": "Ymmydeght", "License": "Kied", "Nothing yet.": "Veg foast.",
    "Prompt": "Glooie", "All": "Ooilley", "Temperature": "Çhiassid", "System": "Corys",
    "Auto": "Seyr-obbragh", "Files": "Coadanyn", "Sign out of this device": "Faill magh ass y saase shoh",
    "Saved": "Sauailt", "New chat": "Resooney noa", "Conversations": "Resoonaghtyn",
    "History": "Shennaghys", "Clear chat": "Glan resooney", "Delete chat": "Scryss resooney",
    "Rename chat": "Aan-enmys resooney", "Tokens": "Cowraghyn", "System prompt": "Glooie y chorys",
    "Skills": "Keirdyn", "Agents": "Jantee", "Storage": "Stoyr", "Network": "Eaddagh-voggyl",
    "Updates": "Noaidyn", "Notifications": "Fysseraghtyn", "Confirm": "Shickyraghey",
    "Yes": "Ta", "No": "Cha nel", "Online": "Er-linney", "Offline": "Neu-linney",
    "Active": "Breeoil", "Connected": "Kianglt", "Disconnected": "Neukianglt",
    "Failed": "Er ny lhie", "Default": "Cadjin", "Version": "Lhieggan",
    "Status": "Stayd", "Details": "Mynphoyntyn", "Account": "Coonteys", "Guest": "Goaldeyr",
    "Appearance": "Cochaslys", "General": "Cadjin", "Audio": "Sheean", "Shortcuts": "Giare-chassyn",
    "Apply": "Cur ayns bree", "Export": "Cur magh", "Import": "Cur stiagh", "Upload": "Laad seose", "Retry": "Prow reesht",
    "Used {n} times": {"one": "Ymmydit {n} cheayrt", "two": "Ymmydit {n} cheayrt", "few": "Ymmydit {n} keayrtyn", "other": "Ymmydit {n} keayrt"},
    "{n} messages left today": {"one": "{n} çhaghteraght faagit jiu", "two": "{n} haghteraght faagit jiu", "few": "{n} çhaghteraghtyn faagit jiu", "other": "{n} çhaghteraght faagit jiu"},
    "{n} pinned apps don’t fit this window": {"one": "Cha nel {n} claare pinneyt jannoo ayns y vyn-uinnag shoh", "two": "Cha nel {n} chlaare pinneyt jannoo ayns y vyn-uinnag shoh", "few": "Cha nel {n} claareyn pinneyt jannoo ayns y vyn-uinnag shoh", "other": "Cha nel {n} claare pinneyt jannoo ayns y vyn-uinnag shoh"},
    "{n} recovery codes left.": {"one": "{n} code aagheddyn faagit.", "two": "{n} chode aagheddyn faagit.", "few": "{n} codeyn aagheddyn faagit.", "other": "{n} code aagheddyn faagit."},
    "{n} services offline": {"one": "{n} hirveish neu-linney", "two": "{n} hirveish neu-linney", "few": "{n} shirveishyn neu-linney", "other": "{n} shirveish neu-linney"}
}

KW = {
    "Cancel": "Hedhi", "Save": "Gwitha", "Delete": "Dilea", "Edit": "Golegi",
    "Download": "Iskarga", "Close": "Degea", "Copy": "Kopïa", "Remove": "Dilea",
    "Name": "Hanow", "Pause": "Powes", "Loading…": "Ow karga…", "Keep": "Gwitha",
    "Resume": "Dastosel", "Dismiss": "Nessa", "Unpin": "Disbina", "Add": "Keworra",
    "Stop": "Sevel", "Title": "Tithel", "Open": "Igeri", "Preview": "Ragwel",
    "Assets": "Pythow", "Off": "Yn-mes", "On": "Yn-fyw", "Create": "Gwruthyl",
    "Today": "Hedhyw", "Accept": "Degemeres", "Copied": "Kopïys", "Settings": "Settyansow",
    "Clear": "Klerhe", "Hide": "Kudha", "Model": "Model", "Agent": "Gwehythor",
    "Skip": "Lemmel", "Rename": "Treylya hanow", "Copy link": "Kopïa kevren",
    "Refresh": "Nowedhi", "Discard": "Tewlel dhe-ves", "Reset": "Dassetya",
    "Unfiled": "Heb restrys", "Collection": "Kuntel", "Send": "Danvon",
    "Generate": "Dinythi", "Favorites": "Kerys", "Activity": "Gweythres",
    "Models": "Modellow", "Search": "Hwilas", "Show": "Diskwedhes", "Continue": "Pesya",
    "Try again": "Assaya arta", "Installed": "Ynstalyes", "Folder": "Kadavell",
    "Projects": "Ragwelyow", "Username": "Hanow-usyer", "Email": "Ebost",
    "Test": "Prow", "Discard your changes?": "Tewlel dhe-ves dha janjyow?", "Good evening": "Gorthugher da",
    "Library": "Lyverva", "Scheduled": "Tewlys", "Notes": "Notennow", "Contacts": "Kestavow",
    "Toggle theme": "Treylya them", "Sign out": "Omdenna", "Sign in": "Omgelmi",
    "Log in": "Omgelmi", "this device": "an devis ma", "Turn off": "Fetha",
    "Done": "Gwrys", "Back": "Dehweles", "Next": "Nessa", "Password": "Ger-tremena",
    "Description": "Deskrifans", "None": "Naneyl", "Mark all read": "Merkya oll redys",
    "Undo": "Diswul", "Mark done": "Merkya gwrys", "Chat": "Keskows",
    "Messages": "Messajys", "New project": "Ragdres nowyth", "Pinned": "Pinys",
    "Queued": "Yn lost", "Size": "Myns", "Check now": "Checkya lemmyn",
    "Delete from disk": "Dilea dhiworth an plasenn", "Used": "Usys", "Stop sharing": "Hedhi ranna",
    "Message": "Messach", "Nothing matches.": "Ny geryth tra vyth.", "Memory": "Kof",
    "Tools": "Toulnow", "Usage": "Devnydh", "License": "Lisyans", "Nothing yet.": "Tra vyth hwath.",
    "Prompt": "Kentryller", "All": "Oll", "Temperature": "Tes", "System": "System",
    "Auto": "Awtomatek", "Files": "Restrennow", "Sign out of this device": "Omdenna dhiworth an devis ma",
    "Saved": "Gwithys", "New chat": "Keskows nowyth", "Conversations": "Keskowsow",
    "History": "Istori", "Clear chat": "Klerhe keskows", "Delete chat": "Dilea keskows",
    "Rename chat": "Treylya hanow keskows", "Tokens": "Arwodhyow", "System prompt": "Kentryller an system",
    "Skills": "Skeulow", "Agents": "Gwehythoryon", "Storage": "Gwithva", "Network": "Ragas",
    "Updates": "Nowedhansow", "Notifications": "Kemenansow", "Confirm": "Afydhya",
    "Yes": "Ya", "No": "Na", "Online": "Warlinen", "Offline": "Dhywarlinen",
    "Active": "Gweythresek", "Connected": "Kelmys", "Disconnected": "Diskelmys",
    "Failed": "Fyllis", "Default": "Defowt", "Version": "Versyon",
    "Status": "Studh", "Details": "Manylyon", "Account": "Akont", "Guest": "Gwestyer",
    "Appearance": "Semlant", "General": "Ollgemmyn", "Audio": "Son", "Shortcuts": "Kevrennow kott",
    "Apply": "Gweytha", "Export": "Esperthi", "Import": "Ymperthi", "Upload": "Uskarga", "Retry": "Assaya arta",
    "Used {n} times": {"one": "Usys {n} gweyth", "two": "Usys {n} weyth", "few": "Usys {n} gweyth", "other": "Usys {n} gweyth"},
    "{n} messages left today": {"one": "{n} messach gesys hedhyw", "two": "{n} vessach gesys hedhyw", "few": "{n} messach gesys hedhyw", "other": "{n} messach gesys hedhyw"},
    "{n} pinned apps don’t fit this window": {"one": "Ny wra {n} gweythres binys fittya y'n fenester ma", "two": "Ny wra {n} weythres binys fittya y'n fenester ma", "few": "Ny wra {n} gweythresow binys fittya y'n fenester ma", "other": "Ny wra {n} gweythres binys fittya y'n fenester ma"},
    "{n} recovery codes left.": {"one": "{n} kod dasgavans gesys.", "two": "{n} god dasgavans gesys.", "few": "{n} kodow dasgavans gesys.", "other": "{n} kod dasgavans gesys."},
    "{n} services offline": {"one": "{n} gonis dhywarlinen", "two": "{n} wonis dhywarlinen", "few": "{n} gonisyow dhywarlinen", "other": "{n} gonis dhywarlinen"}
}

BR = {
    "Cancel": "Nullañ", "Save": "Enrollañ", "Delete": "Dilemel", "Edit": "Aozañ",
    "Download": "Pellgargañ", "Close": "Serriñ", "Copy": "Eilañ", "Remove": "Lemel",
    "Name": "Anv", "Pause": "Ehanañ", "Loading…": "O kargañ…", "Keep": "Mirout",
    "Resume": "Adkregiñ", "Dismiss": "Disteuler", "Unpin": "Dibinañ", "Add": "Ouzhpennañ",
    "Stop": "Paouez", "Title": "Titl", "Open": "Digeriñ", "Preview": "Rakwelet",
    "Assets": "Madoù", "Off": "Diweredekaet", "On": "Gweredekaet", "Create": "Krouiñ",
    "Today": "Hiziv", "Accept": "Asantiñ", "Copied": "Eilet", "Settings": "Arventennoù",
    "Clear": "Skarzhañ", "Hide": "Kuzhat", "Model": "Patrom", "Agent": "Oberer",
    "Skip": "Lammat", "Rename": "Adenvel", "Copy link": "Eilañ al liamm",
    "Refresh": "Freskaat", "Discard": "Disteuler", "Reset": "Adderaouekaat",
    "Unfiled": "Diwrenket", "Collection": "Dastumad", "Send": "Kas",
    "Generate": "Genel", "Favorites": "Re well plijet", "Activity": "Obererezh",
    "Models": "Patromoù", "Search": "Klask", "Show": "Diskouez", "Continue": "Kenderc'hel",
    "Try again": "Klask en-dro", "Installed": "Staliet", "Folder": "Teuliad",
    "Projects": "Raktresoù", "Username": "Anv implijer", "Email": "Postel",
    "Test": "Amprouiñ", "Discard your changes?": "Disteuler ho kemmoù?", "Good evening": "Noz vat",
    "Library": "Levraoueg", "Scheduled": "Steuñvet", "Notes": "Notennoù", "Contacts": "Darempredoù",
    "Toggle theme": "Kemmañ an dodenn", "Sign out": "Digevreañ", "Sign in": "Kevreañ",
    "Log in": "Kevreañ", "this device": "an ardivink-mañ", "Turn off": "Lazhañ",
    "Done": "Graet", "Back": "Distreiñ", "Next": "War-lerc'h", "Password": "Ger-tremen",
    "Description": "Deskrivadur", "None": "Hini ebet", "Mark all read": "Merkañ pep tra evel lennet",
    "Undo": "Dizober", "Mark done": "Merkañ graet", "Chat": "Flapiñ",
    "Messages": "Kemennadoù", "New project": "Raktres nevez", "Pinned": "Bac'het",
    "Queued": "Er roll gortoz", "Size": "Ment", "Check now": "Gwiriañ bremañ",
    "Delete from disk": "Dilemel diwar an disk", "Used": "Implijet", "Stop sharing": "Paouez da rannañ",
    "Message": "Kemennad", "Nothing matches.": "Netra ne glot.", "Memory": "Eñvor",
    "Tools": "Ostilhoù", "Usage": "Implij", "License": "Aotre", "Nothing yet.": "Netra c'hoazh.",
    "Prompt": "Galv", "All": "Pep tra", "Temperature": "Gwrezverk", "System": "Reizhiad",
    "Auto": "Emgefreek", "Files": "Restroù", "Sign out of this device": "Digevreañ diouzh an ardivink-mañ",
    "Saved": "Enrollet", "New chat": "Kaoz nevez", "Conversations": "Kaozeadennoù",
    "History": "Istor", "Clear chat": "Goullonderiñ ar gaoz", "Delete chat": "Dilemel ar gaoz",
    "Rename chat": "Adenvel ar gaoz", "Tokens": "Jedonoù", "System prompt": "Galv ar reizhiad",
    "Skills": "Barregezhioù", "Agents": "Obererien", "Storage": "Stokoù", "Network": "Rouedad",
    "Updates": "Hizivadurioù", "Notifications": "Kemennoù", "Confirm": "Kadarnaat",
    "Yes": "Ya", "No": "Nann", "Online": "Enlinenn", "Offline": "Ezlinenn",
    "Active": "Oberiant", "Connected": "Kevreet", "Disconnected": "Digevreet",
    "Failed": "C'hwitet", "Default": "Dre ziouer", "Version": "Stumm",
    "Status": "Stad", "Details": "Munudoù", "Account": "Kont", "Guest": "Kouviad",
    "Appearance": "Neuz", "General": "Hollek", "Audio": "Klevet", "Shortcuts": "Berradurioù",
    "Apply": "Arloañ", "Export": "Ezporzhañ", "Import": "Enporzhañ", "Upload": "Pellgas", "Retry": "Klask en-dro",
    "Used {n} times": {"one": "Implijet {n} wech", "two": "Implijet {n} wech", "few": "Implijet {n} gwech", "many": "Implijet {n} a wechoù", "other": "Implijet {n} gwech"},
    "{n} messages left today": {"one": "{n} c'hemennad a chom hiziv", "two": "{n} gemennad a chom hiziv", "few": "{n} c'hemennad a chom hiziv", "many": "{n} a gemennadoù a chom hiziv", "other": "{n} kemennad a chom hiziv"},
    "{n} pinned apps don’t fit this window": {"one": "{n} arload pignet ne glot ket gant ar prenestr-mañ", "two": "{n} arload pignet ne glot ket gant ar prenestr-mañ", "few": "{n} arload pignet ne glot ket gant ar prenestr-mañ", "many": "{n} a arloadoù pignet ne glot ket gant ar prenestr-mañ", "other": "{n} arload pignet ne glot ket gant ar prenestr-mañ"},
    "{n} recovery codes left.": {"one": "{n} c'hod adkavout a chom.", "two": "{n} god adkavout a chom.", "few": "{n} c'hod adkavout a chom.", "many": "{n} a godoù adkavout a chom.", "other": "{n} kod adkavout a chom."},
    "{n} services offline": {"one": "{n} servij ezlinenn", "two": "{n} servij ezlinenn", "few": "{n} servij ezlinenn", "many": "{n} a servijoù ezlinenn", "other": "{n} servij ezlinenn"}
}

EU = {
    "Cancel": "Utzi", "Save": "Gorde", "Delete": "Ezabatu", "Edit": "Editatu",
    "Download": "Deskargatu", "Close": "Itxi", "Copy": "Kopiatu", "Remove": "Kendu",
    "Name": "Izena", "Pause": "Pausatu", "Loading…": "Kargatzen…", "Keep": "Mantendu",
    "Resume": "Berrekin", "Dismiss": "Baztertu", "Unpin": "Desiltzatu", "Add": "Gehitu",
    "Stop": "Gelditu", "Title": "Izenburua", "Open": "Ireki", "Preview": "Aurrebista",
    "Assets": "Baliabideak", "Off": "Desaktibatuta", "On": "Aktibatuta", "Create": "Sortu",
    "Today": "Gaur", "Accept": "Onartu", "Copied": "Kopiatuta", "Settings": "Ezarpenak",
    "Clear": "Garbitu", "Hide": "Ezkutatu", "Model": "Eredua", "Agent": "Eragilea",
    "Skip": "Saltatu", "Rename": "Aldatu izena", "Copy link": "Kopiatu esteka",
    "Refresh": "Berritu", "Discard": "Baztertu", "Reset": "Berrezarri",
    "Unfiled": "Sailkatu gabe", "Collection": "Bilduma", "Send": "Bidali",
    "Generate": "Sortu", "Favorites": "Gogokoak", "Activity": "Jarduera",
    "Models": "Ereduak", "Search": "Bilatu", "Show": "Erakutsi", "Continue": "Jarraitu",
    "Try again": "Saiatu berriro", "Installed": "Instalatuta", "Folder": "Karpeta",
    "Projects": "Proiektuak", "Username": "Erabiltzaile-izena", "Email": "Helbide elektronikoa",
    "Test": "Probatu", "Discard your changes?": "Zure aldaketak baztertu?", "Good evening": "Arratsalde on",
    "Library": "Liburutegia", "Scheduled": "Programatuta", "Notes": "Oharrak", "Contacts": "Kontaktuak",
    "Toggle theme": "Aldatu gaia", "Sign out": "Saioa amaitu", "Sign in": "Hasi saioa",
    "Log in": "Saioa hasi", "this device": "gailu hau", "Turn off": "Itzali",
    "Done": "Eginda", "Back": "Atzera", "Next": "Hurrengoa", "Password": "Pasahitza",
    "Description": "Deskribapena", "None": "Bat ere ez", "Mark all read": "Markatu guztiak irakurrita bezala",
    "Undo": "Desegin", "Mark done": "Markatu eginda bezala", "Chat": "Txata",
    "Messages": "Mezuak", "New project": "Proiektu berria", "Pinned": "Ainguratuta",
    "Queued": "Ilaran", "Size": "Tamaina", "Check now": "Egiaztatu orain",
    "Delete from disk": "Ezabatu diskotik", "Used": "Erabilia", "Stop sharing": "Gelditu partekatzea",
    "Message": "Mezua", "Nothing matches.": "Ez dator bat ezerrekin.", "Memory": "Memoria",
    "Tools": "Tresnak", "Usage": "Erabilera", "License": "Lizentzia", "Nothing yet.": "Ezer ez oraindik.",
    "Prompt": "Gonbita", "All": "Guztiak", "Temperature": "Tenperatura", "System": "Sistema",
    "Auto": "Automatikoa", "Files": "Fitxategiak", "Sign out of this device": "Amaitu saioa gailu honetan",
    "Saved": "Gordeta", "New chat": "Txat berria", "Conversations": "Elkarrizketak",
    "History": "Historia", "Clear chat": "Garbitu txata", "Delete chat": "Ezabatu txata",
    "Rename chat": "Aldatu txataren izena", "Tokens": "Tokenak", "System prompt": "Sistemaren gonbita",
    "Skills": "Trebetasunak", "Agents": "Eragileak", "Storage": "Biltegiratzea", "Network": "Sarea",
    "Updates": "Eguneraketak", "Notifications": "Jakinarazpenak", "Confirm": "Baieztatu",
    "Yes": "Bai", "No": "Ez", "Online": "Konektatuta", "Offline": "Deskonektatuta",
    "Active": "Aktibo", "Connected": "Konektatuta", "Disconnected": "Deskonektatuta",
    "Failed": "Huts egin du", "Default": "Lehenetsia", "Version": "Bertsioa",
    "Status": "Egoera", "Details": "Xehetasunak", "Account": "Kontua", "Guest": "Gonbidatua",
    "Appearance": "Itxura", "General": "Orokorra", "Audio": "Audioa", "Shortcuts": "Lasterbideak",
    "Apply": "Aplikatu", "Export": "Esportatu", "Import": "Inportatu", "Upload": "Kargatu", "Retry": "Saiatu berriro",
    "Used {n} times": {"other": "{n} aldiz erabilia"},
    "{n} messages left today": {"other": "{n} mezu geratzen dira gaur"},
    "{n} pinned apps don’t fit this window": {"other": "Ainguratutako {n} aplikazio ez dira sartzen leiho honetan"},
    "{n} recovery codes left.": {"other": "{n} berreskuratze-kode geratzen dira."},
    "{n} services offline": {"other": "{n} zerbitzu lineaz kanpo"}
}

RM = {
    "Cancel": "Interrumper", "Save": "Memorisar", "Delete": "Stizzar", "Edit": "Modifitgar",
    "Download": "Telechargiar", "Close": "Serrar", "Copy": "Copiar", "Remove": "Allontanar",
    "Name": "Num", "Pause": "Pausar", "Loading…": "Chargia…", "Keep": "Mantegnair",
    "Resume": "Reprender", "Dismiss": "Refusar", "Unpin": "Disfissar", "Add": "Agiuntar",
    "Stop": "Fermar", "Title": "Titel", "Open": "Avrir", "Preview": "Prevista",
    "Assets": "Resursas", "Off": "Deactivà", "On": "Activà", "Create": "Crear",
    "Today": "Hoz", "Accept": "Acceptar", "Copied": "Copià", "Settings": "Configuraziun",
    "Clear": "Svidar", "Hide": "Zeler", "Model": "Model", "Agent": "Agent",
    "Skip": "Sursiglir", "Rename": "Renumnar", "Copy link": "Copiar la colliaziun",
    "Refresh": "Actualisar", "Discard": "Refusar", "Reset": "Reinizialisar",
    "Unfiled": "Betg ordinà", "Collection": "Collecziun", "Send": "Trametter",
    "Generate": "Generar", "Favorites": "Favorits", "Activity": "Activitad",
    "Models": "Models", "Search": "Tschertgar", "Show": "Mussar", "Continue": "Cuntinuar",
    "Try again": "Emprovar anc ina giada", "Installed": "Installà", "Folder": "Ordinatur",
    "Projects": "Projects", "Username": "Num d'utilisader", "Email": "E-mail",
    "Test": "Test", "Discard your changes?": "Refusar tias midadas?", "Good evening": "Buna saira",
    "Library": "Biblioteca", "Scheduled": "Plaunì", "Notes": "Notas", "Contacts": "Contacts",
    "Toggle theme": "Midar il design", "Sign out": "Sortir", "Sign in": "S'annunziar",
    "Log in": "S'annunziar", "this device": "quest apparat", "Turn off": "Deactivar",
    "Done": "Terminà", "Back": "Enavos", "Next": "Enavant", "Password": "Ppled-clav",
    "Description": "Descripziun", "None": "Nagut", "Mark all read": "Marcar tut sco legì",
    "Undo": "Revocar", "Mark done": "Marcar sco terminà", "Chat": "Chat",
    "Messages": "Messadis", "New project": "Nov project", "Pinned": "Fissà",
    "Queued": "En colona", "Size": "Grondezza", "Check now": "Verifitgar ussa",
    "Delete from disk": "Stizzar dal disc", "Used": "Utilisà", "Stop sharing": "Chalar da cundivider",
    "Message": "Messadi", "Nothing matches.": "Naginas correspundenzas.", "Memory": "Memoria",
    "Tools": "Utensils", "Usage": "Utilisaziun", "License": "Licenza", "Nothing yet.": "Anc nagut.",
    "Prompt": "Instrucziun", "All": "Tut", "Temperature": "Temperatura", "System": "Sistem",
    "Auto": "Automatic", "Files": "Datotecas", "Sign out of this device": "Sortir da quest apparat",
    "Saved": "Memorisà", "New chat": "Nov chat", "Conversations": "Conversaziuns",
    "History": "Cronologia", "Clear chat": "Svidar il chat", "Delete chat": "Stizzar il chat",
    "Rename chat": "Renumnar il chat", "Tokens": "Segns", "System prompt": "Instrucziun dal sistem",
    "Skills": "Abilitads", "Agents": "Agents", "Storage": "Memoria", "Network": "Rait",
    "Updates": "Actualisaziuns", "Notifications": "Notificaziuns", "Confirm": "Confirmar",
    "Yes": "Gie", "No": "Na", "Online": "Online", "Offline": "Offline",
    "Active": "Activ", "Connected": "Collià", "Disconnected": "Deconnectà",
    "Failed": "Errur", "Default": "Standard", "Version": "Versiun",
    "Status": "Stadi", "Details": "Detagls", "Account": "Conto", "Guest": "Visitader",
    "Appearance": "Optica", "General": "General", "Audio": "Audio", "Shortcuts": "Cumbinaziuns da tastas",
    "Apply": "Applitgar", "Export": "Exportar", "Import": "Importar", "Upload": "Chargiar si", "Retry": "Emprovar anc ina giada",
    "Used {n} times": {"one": "Utilisà {n} giada", "other": "Utilisà {n} giadas"},
    "{n} messages left today": {"one": "Anc {n} messadi oz", "other": "Anc {n} messadis oz"},
    "{n} pinned apps don’t fit this window": {"one": "{n} applicaziun fissada na stat betg en questa fanestra", "other": "{n} applicaziuns fissadas na stattan betg en questa fanestra"},
    "{n} recovery codes left.": {"one": "Anc {n} code da recuperaziun.", "other": "Anc {n} codes da recuperaziun."},
    "{n} services offline": {"one": "{n} survetsch offline", "other": "{n} survetschs offline"}
}

LIV = {
    "Cancel": "Katkāstõ", "Save": "Pästõ", "Delete": "Kistõ", "Edit": "Kohendõ",
    "Download": "Alīzkēratõ", "Close": "Kīndõ", "Copy": "Kopijertõ", "Remove": "Nõstõ",
    "Name": "Nim̄i", "Pause": "Pauzi", "Loading…": "Kēratab…", "Keep": "Piddõ",
    "Resume": "Uudistõ", "Dismiss": "Laiskõ", "Unpin": "Ildõ", "Add": "Jūrkēratõ",
    "Stop": "Seizõ", "Title": "Pǟkēra", "Open": "Avāstõ", "Preview": "Iežvaņtlimi",
    "Assets": "Vārad", "Off": "Vāidleb", "On": "Toimib", "Create": "Lūodõ",
    "Today": "Täuds", "Accept": "Vastõ võttõ", "Copied": "Kopijerttõd", "Settings": "Sēadõkssõd",
    "Clear": "Pūdstõ", "Hide": "Kāndõ", "Model": "Modēl", "Agent": "Toimiji",
    "Skip": "Laskõ ilīz", "Rename": "Nim̄itõ uudīst", "Copy link": "Kopijertõ sidāmst",
    "Refresh": "Uudistõ", "Discard": "Ildõ", "Reset": "Algēz piddõ",
    "Unfiled": "Jagdõmõta", "Collection": "Kogōd", "Send": "Saadõ",
    "Generate": "Lūodõ", "Favorites": "Mīeldidi", "Activity": "Teāgõks",
    "Models": "Modēld", "Search": "Vātsõ", "Show": "Nēitõ", "Continue": "Edīz piddõ",
    "Try again": "Prōvtõ uudīst", "Installed": "Sēadõt", "Folder": "Mapp",
    "Projects": "Projēktõd", "Username": "Kēvātiji nim̄i", "Email": "E-kēra",
    "Test": "Prōv", "Discard your changes?": "Ildõ amād muutõksõd?", "Good evening": "Jõvā ȭdõg",
    "Library": "Rāntõkog", "Scheduled": "Plaanõt", "Notes": "Mēldõpidāmsõd", "Contacts": "Kontāktõd",
    "Toggle theme": "Vaihõtõ tēma", "Sign out": "Ulzõ lēstõ", "Sign in": "Si'zzõ lēstõ",
    "Log in": "Si'zzõ lēstõ", "this device": "sīezõ seāde", "Turn off": "Lopātõ",
    "Done": "Valmõs", "Back": "Taggaz", "Next": "Tūoisti", "Password": "Salasõnā",
    "Description": "Kēraztuz", "None": "Mitte midāgst", "Mark all read": "Mērgõ amād lugdõd",
    "Undo": "Tagānõ", "Mark done": "Mērgõ valmõs", "Chat": "Pajatimiz",
    "Messages": "Sõnād", "New project": "Ūž projēkt", "Pinned": "Kīnditõd",
    "Queued": "Jonos", "Size": "Sūrit", "Check now": "Vaņtlõ nust",
    "Delete from disk": "Kistõ disktõ", "Used": "Kēvātõd", "Stop sharing": "Lopātõ jagāmist",
    "Message": "Sõnā", "Nothing matches.": "Midāgst äb vasta.", "Memory": "Mēldõpidāmi",
    "Tools": "Tīerīistad", "Usage": "Kēvātami", "License": "Litsents", "Nothing yet.": "Äb vel midāgst.",
    "Prompt": "Kutsūmi", "All": "Amād", "Temperature": "Lämpimõt", "System": "Sistēm",
    "Auto": "Automātili", "Files": "Failõd", "Sign out of this device": "Ulzõ lēstõ sīestõ seādest",
    "Saved": "Pästõd", "New chat": "Ūž pajatimi", "Conversations": "Pajatamizõd",
    "History": "Istōrij", "Clear chat": "Pūdstõ pajatimiz", "Delete chat": "Kistõ pajatimiz",
    "Rename chat": "Nim̄itõ pajatimiz uudīst", "Tokens": "Mērgid", "System prompt": "Sistēm kutsūmi",
    "Skills": "Mõistmizõd", "Agents": "Toimijid", "Storage": "Ait", "Network": "Vȭrk",
    "Updates": "Uudīstõksõd", "Notifications": "Teādmizõd", "Confirm": "Kinnitõ",
    "Yes": "Jā", "No": "Äb", "Online": "Vȭrgõs", "Offline": "Ilmā vȭrkõ",
    "Active": "Toimiji", "Connected": "Sidūldõt", "Disconnected": "Ildõt",
    "Failed": "Eksīmi", "Default": "Iežkēraz", "Version": "Versij",
    "Status": "Stātus", "Details": "Mīenpōld", "Account": "Konto", "Guest": "Vīerõz",
    "Appearance": "Iežvaņtli", "General": "Ildimēli", "Audio": "Helī", "Shortcuts": "Līhikērad",
    "Apply": "Kēvātõ", "Export": "Eksportõ", "Import": "Importõ", "Upload": "I'llzkēratõ", "Retry": "Prōvtõ uudīst",
    "Used {n} times": {"one": "{n} kerd kēvātõd", "other": "{n} kerdā kēvātõd"},
    "{n} messages left today": {"one": "Täuds {n} sõnā jä'nd", "other": "Täuds {n} sõnād jä'nd"},
    "{n} pinned apps don’t fit this window": {"one": "{n} kīnditõd app äb ma'ggõ sīezõ lazās", "other": "{n} kīnditõd appõd äb ma'ggõ sīezõ lazās"},
    "{n} recovery codes left.": {"one": "{n} tagānõmiz kōd jä'nd.", "other": "{n} tagānõmiz kōdõd jä'nd."},
    "{n} services offline": {"one": "{n} teenust ilmā vȭrkõ", "other": "{n} teenustõd ilmā vȭrkõ"}
}

SMN = {
    "Cancel": "Keechâ", "Save": "Vuorkkii", "Delete": "Sikkii", "Edit": "Mute",
    "Download": "Lyeđe", "Close": "Toopâ", "Copy": "Kopijist", "Remove": "Vääldi meddâl",
    "Name": "Nommâ", "Pause": "Puddâ", "Loading…": "Luáđá…", "Keep": "Tollâ",
    "Resume": "Jotkâ", "Dismiss": "Hilgo", "Unpin": "Čuolbâ meddâl", "Add": "Lassee",
    "Stop": "Oros", "Title": "Paječala", "Open": "Leehâst", "Preview": "Munetubdâstem",
    "Assets": "Riggoduvah", "Off": "Meddâl", "On": "Álguu", "Create": "Räähi",
    "Today": "Onne", "Accept": "Tuhhit", "Copied": "Kopijistum", "Settings": "Asâttâsah",
    "Clear": "Kurreer", "Hide": "Čiälgât", "Model": "Malli", "Agent": "Tuáimee",
    "Skip": "Njuško paijeel", "Rename": "Mute noomâ", "Copy link": "Kopijist liiŋkâ",
    "Refresh": "Uđâsmit", "Discard": "Heittei", "Reset": "Algâasâttâs",
    "Unfiled": "Juávhuthánnáá", "Collection": "Čoagâldâh", "Send": "Vuolgât",
    "Generate": "Pyevtit", "Favorites": "Rähisumosah", "Activity": "Toimâ",
    "Models": "Maalah", "Search": "Uusâ", "Show": "Čääiti", "Continue": "Juátki",
    "Try again": "Iirât uđđâsist", "Installed": "Asâttum", "Folder": "Mappâ",
    "Projects": "Proojeevteh", "Username": "Kevtteenommâ", "Email": "Šleđgâpostâ",
    "Test": "Iirâttâs", "Discard your changes?": "Heittei muttuidâd?", "Good evening": "Pyeri eehid",
    "Library": "Kirjerááju", "Scheduled": "Áigáduvvum", "Notes": "Muštottâsah", "Contacts": "Ohtâvuodah",
    "Toggle theme": "Mute teema", "Sign out": "Čáládât olgos", "Sign in": "Čáládât siisâ",
    "Log in": "Čáládât siisâ", "this device": "taat tyeji", "Turn off": "Peehti",
    "Done": "Vaalmâš", "Back": "Maasâd", "Next": "Čuávuvâš", "Password": "Syeligâssääni",
    "Description": "Kuvvim", "None": "Ij mihheen", "Mark all read": "Merkkii puoh luohhummin",
    "Undo": "Koomeet", "Mark done": "Merkkii vaalmâžin", "Chat": "Savâstâllâm",
    "Messages": "Tiäđuh", "New project": "Uđđâ proojeekt", "Pinned": "Tevdum",
    "Queued": "Rááđust", "Size": "Stuárudâh", "Check now": "Täärhist tääl",
    "Delete from disk": "Sikkii leevist", "Used": "Kevttum", "Stop sharing": "Oros jyehimist",
    "Message": "Tiätu", "Nothing matches.": "Ij mihheen heivii.", "Memory": "Mušto",
    "Tools": "Tyejiniävuh", "Usage": "Kevttim", "License": "Liseensâ", "Nothing yet.": "Ij vala mihheen.",
    "Prompt": "Ávžuttâs", "All": "Puoh", "Temperature": "Lieggâvuotâ", "System": "Vuáhádâh",
    "Auto": "Automaatlâš", "Files": "Tiätuvuárháh", "Sign out of this device": "Čáládât olgos taam tyejist",
    "Saved": "Vuorkkejum", "New chat": "Uđđâ savâstâllâm", "Conversations": "Savâstâlmeh",
    "History": "Historjá", "Clear chat": "Kurreer savâstâllâm", "Delete chat": "Sikkii savâstâllâm",
    "Rename chat": "Mute savâstâllâm noomâ", "Tokens": "Merkah", "System prompt": "Vuáháduv ávžuttâs",
    "Skills": "Táiđuh", "Agents": "Tuáimeeh", "Storage": "Vuárkká", "Network": "Viermâ",
    "Updates": "Uđâsmitmeh", "Notifications": "Almottâsah", "Confirm": "Nanosmit",
    "Yes": "Joo", "No": "Ij", "Online": "Viermist", "Offline": "Viärmiettáá",
    "Active": "Toimâš", "Connected": "Ohtâvuođâst", "Disconnected": "Ohtâvuotâ potkânâm",
    "Failed": "Feilâ", "Default": "Algâalgâlâš", "Version": "Versio",
    "Status": "Tile", "Details": "Tärhis tiäđuh", "Account": "Konto", "Guest": "Kuási",
    "Appearance": "Olgotiegu", "General": "Almolâš", "Audio": "Jienâ", "Shortcuts": "Uánihispaalgah",
    "Apply": "Kevttii", "Export": "Vuolgât olgos", "Import": "Pyehti siisâ", "Upload": "Vuolgât paasâd", "Retry": "Iirât uđđâsist",
    "Used {n} times": {"one": "{n} tove kevttum", "two": "{n} tove kevttum", "other": "{n} tove kevttum"},
    "{n} messages left today": {"one": "{n} tiätu pääccám onne", "two": "{n} tiäđu pääccám onne", "other": "{n} tiätud pääccám onne"},
    "{n} pinned apps don’t fit this window": {"one": "{n} tevdum heiviittâs ij heivii taan laasân", "two": "{n} tevdum heiviittâs ij heivii taan laasân", "other": "{n} tevdum heiviittâsah iä heivii taan laasân"},
    "{n} recovery codes left.": {"one": "{n} maasâdpajanemkoodi pääccám.", "two": "{n} maasâdpajanemkoodi pääccám.", "other": "{n} maasâdpajanemkoodih pääccám."},
    "{n} services offline": {"one": "{n} palvâlus viärmiettáá", "two": "{n} palvâlus viärmiettáá", "other": "{n} palvâlusah viärmiettáá"}
}

NEW_ENDANGERED = {
    "gv": GV,
    "kw": KW,
    "br": BR,
    "eu": EU,
    "rm": RM,
    "liv": LIV,
    "smn": SMN,
}


def main():
    update_celtic()
    for code, data in NEW_ENDANGERED.items():
        f = LOCALES / f"{code}.json"
        f.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Created/updated {f.name} ({len(data)} entries)")


if __name__ == "__main__":
    main()
