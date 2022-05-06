

class BankAccount:

    def __init__(self, int_rate=.01, balance=0): 
        self.balance = balance
        self.int_rate = int_rate
        

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

account = BankAccount()
account2 = BankAccount()

account.make_deposit(800).make_deposit(1500).make_deposit(75).make_withdraw(400).yield_interest()
account2.make_deposit(900).make_deposit(2000).make_withdraw(85).make_withdraw(45).make_withdraw(64).make_withdraw(5).yield_interest

account.display_account_info()
account2.display_account_info()