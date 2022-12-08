import unittest

from ..BusinessAccount import BusinessAccount
from ..Account import Account


class TestTransferHistory(unittest.TestCase):
    name = "Johny"
    surname = "Krasinski"
    pesel = "01212567891"
    company_name = "Januszex sp. z o.o."
    nip = "8461627563"

    def test_history_new_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        self.assertListEqual(
            account.transfer_history,
            [],
            "Historia transakcji dla nowego konta prywatnego nie jest pusta!",
        )

    def test_history_incoming_transfer_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        account.incoming_transfer(100)
        self.assertListEqual(
            account.transfer_history,
            [100],
            "Przelew przychodzacy nie zostal wpisany do historii!",
        )

    def test_history_outgoing_transfer_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        account.balance = 100
        account.outgoing_transfer(50)
        self.assertListEqual(
            account.transfer_history,
            [-50],
            "Przelew wychodzacy nie zostal wpisany do historii!",
        )

    def test_history_express_transfer_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        account.balance = 100
        account.express_transfer(50)
        self.assertListEqual(
            account.transfer_history,
            [-50, -1],
            "Przelew ekspresowy nie zostal wpisany do historii!",
        )

    def test_history_multiple_transfers_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        account.incoming_transfer(1000)
        account.express_transfer(200)
        account.outgoing_transfer(100)
        self.assertListEqual(
            account.transfer_history,
            [1000, -200, -1, -100],
            "Historia przelewow nie jest poprawna!",
        )

    # Business account

    def test_history_new_business_account(self):
        account = BusinessAccount(self.company_name, self.nip)
        self.assertListEqual(
            account.transfer_history,
            [],
            "Historia transakcji dla nowego konta biznesowego nie jest pusta!",
        )

    def test_history_incoming_transfer_business_account(self):
        account = BusinessAccount(self.company_name, self.nip)
        account.incoming_transfer(100)
        self.assertListEqual(
            account.transfer_history,
            [100],
            "Przelew przychodzacy nie zostal wpisany do historii!",
        )

    def test_history_outgoing_transfer_business_account(self):
        account = BusinessAccount(self.company_name, self.nip)
        account.balance = 100
        account.outgoing_transfer(50)
        self.assertListEqual(
            account.transfer_history,
            [-50],
            "Przelew wychodzacy nie zostal wpisany do historii!",
        )

    def test_history_express_transfer_business_account(self):
        account = BusinessAccount(self.company_name, self.nip)
        account.balance = 100
        account.express_transfer(50)
        self.assertListEqual(
            account.transfer_history,
            [-50, -5],
            "Przelew ekspresowy nie zostal wpisany do historii!",
        )

    def test_history_multiple_transfers_business_account(self):
        account = BusinessAccount(self.company_name, self.nip)
        account.incoming_transfer(1000)
        account.express_transfer(200)
        account.outgoing_transfer(100)
        self.assertListEqual(
            account.transfer_history,
            [1000, -200, -5, -100],
            "Historia przelewow nie jest poprawna!",
        )
