import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12325678912"  # 12.2012r.
    wrong_pesel_info = "Niepoprawny PESEL!"
    correct_promo_code = "PROM-XYZ"

    def test_create_account(self):
        first_account = Konto(self.name, self.surname, self.pesel)

        self.assertEqual(first_account.name, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(
            first_account.surname, self.surname, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(first_account.balance, 0, "Saldo nie jest zerowe!")

        # tutaj proszę dodawać nowe testy

        self.assertEqual(first_account.pesel, self.pesel, "PESEL nie zostal zapisany!")

    def test_pesel_too_short(self):
        pesel = "123"
        account = Konto(self.name, self.surname, pesel)
        self.assertEqual(
            account.pesel, self.wrong_pesel_info, "Podany PESEL jest zbyt krotki!"
        )

    def test_pesel_too_long(self):
        pesel = "1241415161666727"
        account = Konto(self.name, self.surname, pesel)
        self.assertEqual(
            account.pesel, self.wrong_pesel_info, "Podany PESEL jest zbyt dlugi!"
        )

    def test_account_correct_promo_code(self):
        bonus_srodki = 50
        account = Konto(self.name, self.surname, self.pesel, self.correct_promo_code)

        self.assertEqual(
            account.balance, bonus_srodki, "Bonusowe srodki nie zostaly dodane!"
        )

    def test_account_wrong_promo_code(self):
        promo_code = "DARMOWE_5_DYSZEK"
        account = Konto(self.name, self.surname, self.pesel, promo_code)

        self.assertEqual(
            account.balance, 0, "Bonusowe srodki zostaly dodane mimo zlego kodu!"
        )

    def test_born_before_1900(self):
        pesel = "99811234567"  # 01.1899r.
        account = Konto(self.name, self.surname, pesel, self.correct_promo_code)

        self.assertEqual(
            account.balance, 0, "Bonusowe srodki zostaly przyznane seniorowi!"
        )

    def test_born_before_1961(self):
        pesel = "60011234567"  # 01.1960r.
        account = Konto(self.name, self.surname, pesel, self.correct_promo_code)

        self.assertEqual(
            account.balance, 0, "Bonusowe srodki zostaly przyznane seniorowi!"
        )
