"""
Skripta za isporuku (deploy) aplikacije.
Pokrece Flask aplikaciju kao samostalan pozadinski proces na portu 5001
te provjerava radi li aplikacija pozivom na /health endpoint (smoke test).

Koristi se u Deploy fazi Jenkins pipelinea.
"""

import subprocess
import sys
import time
import urllib.request
import os

PORT = 5001
HEALTH_URL = f"http://localhost:{PORT}/health"
PID_DATOTEKA = "deploy_pid.txt"


def zaustavi_prethodnu_instancu():
    """Zaustavlja prethodno pokrenutu instancu aplikacije ako postoji."""
    if os.path.exists(PID_DATOTEKA):
        try:
            with open(PID_DATOTEKA, "r") as f:
                stari_pid = f.read().strip()
            if stari_pid:
                # Windows naredba za zaustavljanje procesa prema PID-u
                subprocess.run(
                    ["taskkill", "/F", "/PID", stari_pid],
                    capture_output=True
                )
                print(f"Zaustavljena prethodna instanca (PID {stari_pid}).")
        except Exception as e:
            print(f"Napomena: nije moguce zaustaviti prethodnu instancu: {e}")


def pokreni_aplikaciju():
    """Pokrece aplikaciju kao samostalan proces neovisan o Jenkinsu."""
    python_exe = os.path.join("venv", "Scripts", "python.exe")

    # Postavljanje porta preko varijable okruzenja
    okruzenje = os.environ.copy()
    okruzenje["PORT"] = str(PORT)

    # Uklanjanje Jenkins varijabli okruzenja kojima ProcessTreeKiller
    # prepoznaje i zaustavlja procese pokrenute tijekom builda.
    # Bez njih aplikacija nastavlja raditi i nakon zavrsetka pipelinea.
    for varijabla in ("JENKINS_NODE_COOKIE", "JENKINS_SERVER_COOKIE", "BUILD_ID", "HUDSON_COOKIE"):
        okruzenje.pop(varijabla, None)

    # DETACHED_PROCESS (0x00000008) + CREATE_NEW_PROCESS_GROUP (0x00000200)
    # cine proces samostalnim i neovisnim o procesu koji ga je pokrenuo.
    proces = subprocess.Popen(
        [python_exe, "app.py"],
        env=okruzenje,
        creationflags=0x00000008 | 0x00000200,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Spremanje PID-a za buduce zaustavljanje
    with open(PID_DATOTEKA, "w") as f:
        f.write(str(proces.pid))

    print(f"Aplikacija pokrenuta (PID {proces.pid}) na portu {PORT}.")
    return proces.pid


def provjeri_zdravlje():
    """Smoke test - provjerava odgovara li aplikacija na /health."""
    print("Cekanje da se aplikacija pokrene...")
    for pokusaj in range(1, 11):
        try:
            with urllib.request.urlopen(HEALTH_URL, timeout=2) as odgovor:
                if odgovor.status == 200:
                    sadrzaj = odgovor.read().decode()
                    print(f"Smoke test uspjesan! Aplikacija odgovara: {sadrzaj}")
                    return True
        except Exception:
            print(f"  Pokusaj {pokusaj}/10 - aplikacija jos nije spremna...")
            time.sleep(1)
    print("Smoke test neuspjesan - aplikacija ne odgovara.")
    return False


if __name__ == "__main__":
    print("=== Pokretanje procesa isporuke ===")
    zaustavi_prethodnu_instancu()
    pokreni_aplikaciju()
    uspjeh = provjeri_zdravlje()

    if uspjeh:
        print("=== Isporuka uspjesno zavrsena ===")
        sys.exit(0)
    else:
        print("=== Isporuka neuspjesna ===")
        sys.exit(1)
