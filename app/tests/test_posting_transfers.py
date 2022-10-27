import unittest

from ..Konto import Konto

class TestPostingTransfers(unittest.TestCase):
  name = "Dariusz"
  surname = "Januszewski"
  pesel = "12325678912"  # 12.2012r.
  
  def test_incoming_transfer(self):
    account = Konto(self.name, self.surname, self.pesel)
    account._saldo = 300
    account.incoming_transfer(500)

    self.assertEqual(account.saldo, 800, "Srodki nie zostaly dodane!")

  def test_outgoing_transfer_with_not_enough_money(self):
    account = Konto(self.name, self.surname, self.pesel)
    account._saldo = 300
    account.outgoing_transfer(500)

    self.assertEqual(account.saldo, 300, "Srodki zostaly odjete mimo braku funduszy na koncie!")

  def test_outgoing_transfer_with_enough_money(self):
    account = Konto(self.name, self.surname, self.pesel)
    account._saldo = 1000
    account.outgoing_transfer(500)

    self.assertEqual(account.saldo, 500, "Srodki nie zostaly wyjete z konta!")