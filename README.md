# CI/CD Profiles Generator 🚀

![PIPELINE](https://github.com/JakobBrandelNackadmin/ci-cd-profiles-jakob/actions/workflows/main.yml/badge.svg)

Detta projekt genererar kundprofiler och publicerar dem automatiskt på en publik webbplats via GitHub Pages – med full CI/CD pipeline.

## 🔧 Funktionalitet

- Skapar `profiles1.csv` med fejkdata via `generate.py` (med Faker)
- Konverterar CSV till JSON (`data.json`) via `csvtojson.py`
- Kör enhetstester på CSV och JSON
- Publicerar `index.html` + `script.js` + `data.json` till GitHub Pages

## 🔁 CI/CD PIPELINE

Byggs och deployas automatiskt vid varje push till `main`:

```yaml
✅ generate.py
✅ csvtojson.py
✅ pytest tester
✅ deploy till GitHub Pages
```

## 🧪 Tester

Testerna verifierar:
- CSV har exakt 12 kolumner
- CSV har 900+ rader
- JSON-filen är korrekt strukturerad och matchar CSV

## 🌐 Publik länk

[📎 Gå till webbplatsen här](https://jakobbrandelnackadmin.github.io/ci-cd-profiles-jakob/)

## ▶️ Köra lokalt

```bash
pip install -r requirements.txt  # eller pip install faker pytest
python generate.py
python csvtojson.py
pytest
```

## 🛠 Verktyg

- Python 3.12
- Faker
- Pytest
- GitHub Actions