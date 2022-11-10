import unittest

from ..Account import Account


class TestTakingLoan(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12325678912"

    def test_three_history_records_income(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [-100, 100, 100, 100]
        is_granted = account.take_loan(700)

        self.assertTrue(is_granted)
        self.assertEqual(account.balance, 700)

    def test_three_history_records_not_income(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [-100, 100, -100, 100]
        is_granted = account.take_loan(700)

        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_two_history_records_income(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [100, 100]
        is_granted = account.take_loan(700)

        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_five_history_records_more_than_loan(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [-100, -100, 400, -100, 100, -100]
        is_granted = account.take_loan(199)

        self.assertTrue(is_granted)
        self.assertEqual(account.balance, 199)

    def test_five_history_records_less_equal_than_loan(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [-100, -100, 400, -100, 100, -100]
        is_granted = account.take_loan(200)

        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_four_history_records_more_than_loan(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = [400, -100, 100, -100]
        is_granted = account.take_loan(200)

        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)

    def test_zero_history_records(self):
        account = Account(self.name, self.surname, self.pesel)
        account.transfer_history = []
        is_granted = account.take_loan(200)

        self.assertFalse(is_granted)
        self.assertEqual(account.balance, 0)
