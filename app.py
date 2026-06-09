from flask import Flask, jsonify, request
from utils import formatiraj_pozdrav, zbroji

app = Flask(__name__)

POCETNA_HTML = """
<!DOCTYPE html>
<html lang="hr">
<head>
    <meta charset="UTF-8">
    <title>CI/CD Demo aplikacija</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9;
               display: flex; justify-content: center; align-items: center;
               height: 100vh; margin: 0; }
        .kartica { background: white; padding: 40px 60px; border-radius: 12px;
                   box-shadow: 0 4px 20px rgba(0,0,0,0.08); text-align: center; }
        h1 { color: #1a3c6e; margin-bottom: 8px; }
        p { color: #5a6b82; }
        .verzija { margin-top: 20px; font-size: 13px; color: #9aa7b8; }
    </style>
</head>
<body>
    <div class="kartica">
        <h1>CI/CD Demo aplikacija</h1>
        <p>Implementacija CI/CD procesa u razvoju web aplikacije</p>
        <p class="verzija">Verzija 1.0 &middot; Fran Alpeza</p>
    </div>
</body>
</html>
"""


@app.route("/")
def pocetna():
    return POCETNA_HTML


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/pozdrav")
def pozdrav():
    ime = request.args.get("ime", "")
    return jsonify({"poruka": formatiraj_pozdrav(ime)})


@app.route("/zbroj")
def zbroj():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"rezultat": zbroji(a, b)})
    except ValueError:
        return jsonify({"greska": "Parametri moraju biti brojevi"}), 400


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
