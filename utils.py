def zbroji(a, b):
    return a + b


def je_paran(broj):
    return broj % 2 == 0


def formatiraj_pozdrav(ime):
    if not ime:
        return "Pozdrav, gostu!"
    return f"Pozdrav, {ime}!"
