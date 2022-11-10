import re


def pesel_processing(pesel):
    if len(pesel) == 11:
        return pesel
    else:
        return "Niepoprawny PESEL!"


def is_promo_code_wrong(promo_code):
    if promo_code is None or re.fullmatch("^PROM-.{3}$", promo_code) is None:
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

def transform_negative_val_to_zero(num: int):
    if num > 0:
        return num
    else:
        return 0


class Account:
    express_transfer_commission = 1

    def __init__(self, name, surname, pesel, promo_code=None):
        self.name = name
        self.surname = surname
        self.pesel = pesel_processing(pesel)
        self.balance = initial_balance(self.pesel, promo_code)
        self.transfer_history = []

    def incoming_transfer(self, amount):
        self.balance += amount
        self.transfer_history.append(amount)

    def outgoing_transfer(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.transfer_history.append(-amount)

    def express_transfer(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount - self.express_transfer_commission
            self.transfer_history.extend([-amount, -self.express_transfer_commission])

    def take_loan(self, amount):
        if len(self.transfer_history) < 3:
            return False
        if len(self.transfer_history) >= 5:
            last_five_transfers = []
            last_five_transfers.extend(self.transfer_history[-5:])
            history_sum = sum(last_five_transfers)
            if history_sum > amount:
                self.balance += amount
                return True
        if len(self.transfer_history) >= 3:
            last_three_transfers = []
            last_three_transfers.extend(self.transfer_history[-3:])
            history_mod = list(map(transform_negative_val_to_zero, last_three_transfers))
            if all(history_mod):
                self.balance += amount
                return True
        return False
