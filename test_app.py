"""
Automatizirani testovi aplikacije.
Pokrecu se pomocu naredbe: pytest

Testovi su podijeljeni na testove HTTP ruta i testove pomocnih funkcija.
"""

import pytest
from app import app
from utils import zbroji, je_paran, formatiraj_pozdrav


@pytest.fixture
def client():
    """Priprema testnog klijenta za slanje zahtjeva aplikaciji."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- Testovi HTTP ruta ---

def test_pocetna_vraca_200(client):
    """Pocetna stranica mora vratiti status 200."""
    odgovor = client.get("/")
    assert odgovor.status_code == 200


def test_health_vraca_ok(client):
    """Health endpoint mora vratiti status 'ok'."""
    odgovor = client.get("/health")
    assert odgovor.status_code == 200
    assert odgovor.get_json()["status"] == "ok"


def test_pozdrav_s_imenom(client):
    """Endpoint pozdrava mora vratiti personaliziranu poruku."""
    odgovor = client.get("/pozdrav?ime=Fran")
    assert odgovor.status_code == 200
    assert odgovor.get_json()["poruka"] == "Pozdrav, Fran!"


def test_zbroj_ispravan_rezultat(client):
    """Endpoint zbroja mora vratiti tocan rezultat."""
    odgovor = client.get("/zbroj?a=2&b=3")
    assert odgovor.status_code == 200
    assert odgovor.get_json()["rezultat"] == 5


# --- Testovi pomocnih funkcija ---

def test_zbroji():
    assert zbroji(2, 3) == 5
    assert zbroji(-1, 1) == 0


def test_je_paran():
    assert je_paran(4) is True
    assert je_paran(5) is False


def test_formatiraj_pozdrav():
    assert formatiraj_pozdrav("Fran") == "Pozdrav, Fran!"
    assert formatiraj_pozdrav("") == "Pozdrav, gostu!"
