from src.users.user import User

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def view_all_accounts(self, accounts):
        for acc in accounts:
            print(f"{acc.name} ({acc.acc_no}): Balance = {acc.balance}")
