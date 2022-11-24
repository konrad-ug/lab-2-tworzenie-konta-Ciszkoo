import unittest

from ..Account import Account
from ..AccountsRegister import AccountsRegister

class TestAccountsRegister(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12325678912"

    def test_adding_first_account(self):
        account = Account(self.name, self.surname, self.pesel)
        AccountsRegister.add_account(account)
        self.assertEqual(AccountsRegister.number_of_accounts(), 1)

    def test_adding_second_account(self):
        account = Account(self.name, self.surname, "12325768912")
        AccountsRegister.add_account(account)
        self.assertEqual(AccountsRegister.number_of_accounts(), 2)

    def test_adding_third_account(self):
        account = Account(self.name, self.surname, self.pesel)
        AccountsRegister.add_account(account)
        self.assertEqual(AccountsRegister.number_of_accounts(), 3)

    def test_searching_for_existing_account(self):
        account = AccountsRegister.find_account("12325768912")
        self.assertEqual(account.pesel, "12325768912")

    def test_searching_for_non_existing_account(self):
        account = AccountsRegister.find_account("02325768910")
        self.assertEqual(account, None)