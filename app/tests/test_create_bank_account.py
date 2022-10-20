import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678912"
    komunikat_zly_pesel = "Niepoprawny PESEL!"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)

        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(
            pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

        # tutaj proszę dodawać nowe testy

        self.assertEqual(pierwsze_konto.pesel, self.pesel, "PESEL nie zostal zapisany!")

    def test_zbyt_krotki_pesel(self):
        pesel = "123"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(
            konto.pesel, self.komunikat_zly_pesel, "Podany PESEL jest zbyt krotki!"
        )

    def test_zbyt_dlugi_pesel(self):
        pesel = "1241415161666727"
        konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(
            konto.pesel, self.komunikat_zly_pesel, "Podany PESEL jest zbyt dlugi!"
        )

    def test_konto_kod_prmocyjny(self):
        kod_promocyjny = "PROM-XYZ"
        bonus_srodki = 50
        konto = Konto(self.imie, self.nazwisko, self.pesel, kod_promocyjny)

        self.assertEqual(
            konto.saldo, bonus_srodki, "Bonusowe srodki nie zostaly dodane!"
        )

    def test_zly_kod_promocyjny(self):
        kod_promocyjny = "DARMOWE_5_DYSZEK"
        konto = Konto(self.imie, self.nazwisko, self.pesel, kod_promocyjny)

        self.assertEqual(
            konto.saldo, 0, "Bonusowe srodki zostaly dodane mimo zlego kodu!"
        )
