class User:


    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

julien = User("Julien")
bob = User("Bob")
max = User("Max")

julien.make_deposit(100)
julien.make_deposit(300)
julien.make_deposit(25)
julien.make_withdrawl(65)

bob.make_deposit(37)
bob.make_deposit(45)
bob.make_withdrawl(15)
bob.make_withdrawl(20)

max.make_deposit(999)
max.make_withdrawl(222)
max.make_withdrawl(333)
max.make_withdrawl(111)

julien.display_user_balance()
bob.display_user_balance()
max.display_user_balance()