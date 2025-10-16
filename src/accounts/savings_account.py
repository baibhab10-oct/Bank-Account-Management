from src.accounts.account import Account

class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance=0, interest_rate=0.03):
        super().__init__(acc_no, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")
