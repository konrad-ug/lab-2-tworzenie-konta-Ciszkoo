import unittest
from unittest.mock import patch, Mock

from ..BusinessAccount import BusinessAccount
from ..Account import Account


class TestExpressTransfer(unittest.TestCase):
    name = "Johny"
    surname = "Krasinski"
    pesel = "01212567891"
    company_name = "Januszex sp. z o.o."
    nip = "8461627563"

    def _mock_response(self, status):
        return Mock(status_code=status)

    def test_express_transfer_normal_account(self):
        account = Account(self.name, self.surname, self.pesel)
        account.balance = 100
        account.express_transfer(100)

        self.assertEqual(
            account.balance, -1, "Prowizja za przelew ekspresowy nie zostala pobrana!"
        )

    def test_express_transfer_normal_account_not_enough_money(self):
        account = Account(self.name, self.surname, self.pesel)
        account.balance = 100
        account.express_transfer(101)

        self.assertEqual(
            account.balance,
            100,
            "Przelew ekspresowy zostal zaksiegowany mimo braku srodkow!",
        )

    @patch('requests.get')
    def test_express_transfer_business_account(self, mock_get):
        mock_response = self._mock_response(200)
        mock_get.return_value = mock_response
        account = BusinessAccount(self.company_name, self.nip)
        account.balance = 100
        account.express_transfer(100)

        self.assertEqual(
            account.balance, -5, "Prowizja za przelew ekspresowy nie zostala pobrana!"
        )

    @patch('requests.get')
    def test_express_transfer_business_account_not_enough_money(self, mock_get):
        mock_response = self._mock_response(200)
        mock_get.return_value = mock_response
        account = BusinessAccount(self.company_name, self.nip)
        account.balance = 100
        account.express_transfer(101)

        self.assertEqual(
            account.balance,
            100,
            "Przelew ekspresowy zostal zaksiegowany mimo braku srodkow!",
        )
