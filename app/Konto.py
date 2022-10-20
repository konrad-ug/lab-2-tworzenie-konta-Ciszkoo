import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, promo_kod = None):
        self.imie = imie
        self.nazwisko = nazwisko

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny PESEL!"

        if promo_kod == None or re.fullmatch("^PROM-.{3}$", promo_kod) == None:
            self.saldo = 0
        else:
            self.saldo = 50
