from .Account import Account


def nip_processing(nip):
    if len(nip) == 10:
        return nip
    else:
        return "Niepoprawny NIP!"


class BusinessAccount(Account):
    express_transfer_commission = 5

    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip_processing(nip)
        self.balance = 0
        self.transfer_history = []

    def take_loan(self, amount):
        if (
            self.balance >= amount * 2
            and len(list(filter(lambda x: x == -1775, self.transfer_history))) > 0
        ):
            self.balance += amount
            return True
        return False
