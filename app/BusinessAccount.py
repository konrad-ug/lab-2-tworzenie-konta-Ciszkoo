from .Account import Account


def nip_processing(nip):
    if len(nip) == 10:
        return nip
    else:
        return "Niepoprawny NIP!"


class BusinessAccount(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip_processing(nip)
        self.balance = 0
        self.express_transfer_commission = 5
