import unittest

from ..BusinessAccount import BusinessAccount


class TestCreateBusinessAccount(unittest.TestCase):
    company_name = "Januszex sp. z o.o."
    correct_nip = "1357924681"
    wrong_nip_info = "Niepoprawny NIP!"

    def test_create_business_account(self):
        account = BusinessAccount(self.company_name, self.correct_nip)

        self.assertEqual(
            account.company_name,
            self.company_name,
            "nazwa firmy nie zostala ustawiona!",
        )
        self.assertEqual(
            account.nip, self.correct_nip, "Nip firmy nie zostal ustawiony"
        )
        self.assertEqual(account.balance, 0, "Saldo konta nie wynosi zero!")

    def test_create_business_account_nip_too_long(self):
        nip_too_long = "11234567891"
        account = BusinessAccount(self.company_name, nip_too_long)

        self.assertEqual(
            account.nip,
            self.wrong_nip_info,
            "Komunikat o niepoprawnym nipie nie zostal nadany!",
        )

    def test_create_business_account_nip_too_short(self):
        nip_too_short = "112345678"
        account = BusinessAccount(self.company_name, nip_too_short)

        self.assertEqual(
            account.nip,
            self.wrong_nip_info,
            "Komunikat o niepoprawnym nipie nie zostal nadany!",
        )
