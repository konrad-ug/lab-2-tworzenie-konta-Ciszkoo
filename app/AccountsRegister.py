from app.Account import Account


class AccountsRegister():
    accounts = []

    @classmethod
    def add_account(self, account: Account) -> None:
        self.accounts.append(account)

    @classmethod
    def number_of_accounts(self) -> int:
        return len(self.accounts)

    @classmethod
    def find_account(self, pesel: str) -> Account | None:
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
