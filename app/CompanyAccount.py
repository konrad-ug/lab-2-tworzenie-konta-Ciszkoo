from .Account import Account


def nip_processing(nip):
    if len(nip) == 10:
        return nip
    else:
        return "Niepoprawny NIP!"


class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip
        self._balance = 0
        self.express_transfer_commission = 5


    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self, nip):
        self._nip = nip_processing(nip)

    @property
    def balance(self):
        return self._balance
