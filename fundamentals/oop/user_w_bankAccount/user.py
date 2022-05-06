from bank_account import BankAccount

class User:


    def __init__(self,name, account):
        self.name = name
        self.account = account
        print(self.account)

    def deposit(self, amount):
        self.account.make_deposit(amount)

    def withdrawl(self, amount):
        self.account.make_withdrawl(amount)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_account_info()}")

account = BankAccount()

julien = User("Julien", account)
