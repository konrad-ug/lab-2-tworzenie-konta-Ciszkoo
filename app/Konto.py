import re


def pesel_poprawnosc(pesel):
    if len(pesel) == 11:
        return pesel
    else:
        return "Niepoprawny PESEL!"


def czy_promo_kod_zly(promo_kod):
    if promo_kod == None or re.fullmatch("^PROM-.{3}$", promo_kod) == None:
        return True
    else:
        return False


def czy_senior(pesel):
    rok_suffix = int(pesel[0:2])
    rok_prefix = int(pesel[2:4])

    if (
        pesel == "Niepoprawny PESEL!"
        or rok_prefix > 80
        or (rok_prefix <= 12 and rok_suffix < 61)
    ):
        return True
    else:
        return False


def saldo_poczatkowe(pesel, promo_kod):
    if czy_promo_kod_zly(promo_kod) or czy_senior(pesel):
        return 0
    else:
        return 50


class Konto:
    def __init__(self, imie, nazwisko, pesel, promo_kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.saldo = (pesel, promo_kod)

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, pesel):
        self._pesel = pesel_poprawnosc(pesel)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, args):
        pesel, promo_kod = args
        self._saldo = saldo_poczatkowe(pesel, promo_kod)
