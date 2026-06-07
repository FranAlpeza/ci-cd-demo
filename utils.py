"""
Pomocne funkcije aplikacije.
Izdvojene su u zaseban modul kako bi se mogle jednostavno testirati.
"""


def zbroji(a, b):
    """Vraca zbroj dvaju brojeva."""
    return a + b


def je_paran(broj):
    """Vraca True ako je broj paran, inace False."""
    return broj % 2 == 0


def formatiraj_pozdrav(ime):
    """Vraca personaliziranu poruku pozdrava."""
    if not ime:
        return "Pozdrav, gostu!"
    return f"Pozdrav, {ime}!"
