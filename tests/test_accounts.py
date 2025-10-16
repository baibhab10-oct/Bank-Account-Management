from src.accounts.account import Account

def test_deposit():
    acc = Account(1, "John", 100)
    acc.deposit(50)
    assert acc.balance == 150

if __name__ == "__main__":
    test_deposit()
    print("All tests passed ✅")
