from src.accounts.account import Account

class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance=0, overdraft_limit=5000):
        super().__init__(acc_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
