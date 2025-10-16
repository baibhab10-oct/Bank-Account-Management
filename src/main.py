from src.accounts.account import Account
from src.accounts.savings_account import SavingsAccount
from src.accounts.current_account import CurrentAccount

def main():
    print("Welcome to the Bank Account Management System")

    acc1 = SavingsAccount(1001, "Alice", 2000)
    acc1.deposit(500)
    acc1.add_interest()

    acc2 = CurrentAccount(1002, "Bob", 1500)
    acc2.withdraw(1000)

if __name__ == "__main__":
    main()
