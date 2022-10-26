import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, promo_kod=None):
        self.imie = imie
        self.nazwisko = nazwisko

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny PESEL!"

        _rok_suffix = int(pesel[0:2])
        rok_prefix = int(pesel[2:4])

        if promo_kod == None or re.fullmatch("^PROM-.{3}$", promo_kod) == None:
            self.saldo = 0
        elif (
            self.pesel == "Niepoprawny PESEL!"
            or rok_prefix > 80
            or (rok_prefix <= 12 and _rok_suffix < 61)
        ):
            self.saldo = 0
        else:
            self.saldo = 50
