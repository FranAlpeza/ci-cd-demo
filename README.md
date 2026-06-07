# CI/CD Demo aplikacija

Jednostavna web aplikacija izrađena u Flask okviru koja služi kao demonstracijski
objekt za implementaciju CI/CD procesa korištenjem alata Jenkins.

**Završni rad** — Implementacija CI/CD procesa u razvoju web aplikacije
Fran Alpeza, Veleučilište Velika Gorica

## Pokretanje aplikacije lokalno

```bash
# 1. Kreiraj virtualno okruzenje
python -m venv venv

# 2. Aktiviraj ga (Windows)
venv\Scripts\activate

# 3. Instaliraj ovisnosti
pip install -r requirements.txt

# 4. Pokreni aplikaciju
python app.py
```

Aplikacija je dostupna na adresi: http://localhost:5000

## Pokretanje testova

```bash
pytest
```

## Rute aplikacije

| Ruta | Opis |
|------|------|
| `/` | Početna stranica |
| `/health` | Provjera zdravlja aplikacije |
| `/pozdrav?ime=Fran` | Personalizirana poruka |
| `/zbroj?a=2&b=3` | Zbroj dvaju brojeva |
