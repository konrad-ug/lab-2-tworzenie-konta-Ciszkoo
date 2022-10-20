import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel)
        pesel = "12345678912"

        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(
            pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        # tutaj proszę dodawać nowe testy

        self.assertEqual(pierwsze_konto.pesel, pesel, "PESEL nie zostal zapisany!")

    def test_tworzenie_konta_zbyt_krotki_pesel(self):
        pesel = "123"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(konto.pesel, "Niepoprawny PESEL!", "Podany PESEL jest zbyt krotki!")

    def test_tworzenie_konta_zbyt_dlugi_pesel(self):
        pesel = "1241415161666727"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(konto.pesel, "Niepoprawny PESEL!", "Podany PESEL jest zbyt dlugi!")
