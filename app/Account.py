import re


def pesel_processing(pesel):
    if len(pesel) == 11:
        return pesel
    else:
        return "Niepoprawny PESEL!"


def is_promo_code_wrong(promo_code):
    if promo_code == None or re.fullmatch("^PROM-.{3}$", promo_code) == None:
        return True
    else:
        return False


def is_senior(pesel):
    year_suffix = int(pesel[0:2])
    year_prefix = int(pesel[2:4])

    if (
        pesel == "Niepoprawny PESEL!"
        or year_prefix > 80
        or (year_prefix <= 12 and year_suffix < 61)
    ):
        return True
    else:
        return False


def initial_balance(pesel, promo_code):
    if is_promo_code_wrong(promo_code) or is_senior(pesel):
        return 0
    else:
        return 50


class Account:
    def __init__(self, name, surname, pesel, promo_code=None):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.balance = (pesel, promo_code)

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, pesel):
        self._pesel = pesel_processing(pesel)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, args):
        pesel, promo_code = args
        self._balance = initial_balance(pesel, promo_code)

    def incoming_transfer(self, amount):
        self._balance += amount

    def outgoing_transfer(self, amount):
        if self.balance > amount:
            self._balance -= amount