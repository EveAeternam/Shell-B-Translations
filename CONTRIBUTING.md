# Contributing a translation

1. Fork the repository. New language: copy `locales/fr.json` to `locales/<code>.json` and translate the values, keys
   untouched, placeholders kept. Improving one: edit the file in place.
2. Add or update the entry in `locales.json` (language name in the language itself, `author`, optional `authorUrl`,
   `license`). By opening a pull request you agree the catalogue is shared under that license.
3. Run `python3 -I scripts/validate.py` from the repository root; fix errors, read the warnings (stale keys are
   usually strings Shell:B renamed; drop or update them).
4. Commit the catalogue, `locales.json`, `index.json` and `README.md` (the script rewrites its table) and open a pull
   request; the template has the checklist. Without git, open a *Submit a translation* issue and attach the file.

Tone: Shell:B talks like a capable colleague, in short sentences, without marketing voice; mirror `fr.json`.
Machine-translated catalogues are accepted as a starting point only if they say so and someone has read them through.
