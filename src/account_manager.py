import logging
import csv

class Account:
    def __init__(self, username: str, password: str, status: bool = None, path: str = None):
        self.username = username
        self.password = password
        self.status = status
        self.path = path


class AccountRepository:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: Account) -> int:
        self.accounts.append(account)
        return len(self.accounts)

    def get_account(self) -> Account:
        selected_account = self.accounts[0]
        self.accounts.remove(selected_account)
        self.accounts.append(selected_account)
        logging.info(f"Selectad account: {selected_account.username}")
        return selected_account

    def update_single_account(self, account: Account):
        target_username = account.username
        for item in self.accounts:
            if item.username == target_username:
                self.accounts.remove(item)
                self.accounts.append(account)
                return self.accounts.index(account)         
        logging.error("no username found")


    def export_repository(self):
        headers = list(self.accounts[0].keys())
        with open('accounts.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.accounts)
            logging.info("Accounts exported to accounts.csv")
        return
