import unittest
from parameterized import parameterized

from ..BusinessAccount import BusinessAccount


class TestTakingLoanCompany(unittest.TestCase):
    company_name = "Januszex sp. z o.o."
    nip = "8461627563"

    def setUp(self) -> None:
        self.account = BusinessAccount(self.company_name, self.nip)

    @parameterized.expand(
        [
            ([100, -100, -1775, 100], 1000, 500, True, 1500),
            ([-1775], 10000, 500, True, 10500),
            ([100, -100, -1775, 100], 1000, 501, False, 1000),
            ([100, -100, 100], 1000, 500, False, 1000),
            ([100, -100, 100], 1000, 501, False, 1000),
            ([], 1000, 500, False, 1000),
        ]
    )
    def test_taking_loan_company(
        self, history, balance, amount, expected_outcome, expected_balance
    ):
        self.account.transfer_history = history
        self.account.balance = balance
        is_granted = self.account.take_loan(amount)

        self.assertEqual(is_granted, expected_outcome)
        self.assertEqual(self.account.balance, expected_balance)
