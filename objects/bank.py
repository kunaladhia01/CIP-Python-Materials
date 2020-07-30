# Bank class
# money
# __init__, deposit(), and withdraw()

class Bank:
    money = 0

    def __init__(self, money):
        self.money = money

    def deposit(self, amount):
        self.money += amount
        return self.money

    def withdraw(self, amount):
        if amount > self.money:
            return "Error"
        else:
            self.money -= amount
            return self.money

# Person class
# name, budget
# __init__(), withdraw(), deposit()
class Person:
    name = ""
    budget = 0

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def deposit(self, bank, amount):
        if amount > self.budget:
            return "Error"
        else:
            self.budget -= amount
            bank.deposit(amount)
            return self.budget

    def withdraw(self, bank, amount):
        x = bank.withdraw(amount)
        if x == "Error":
            return "Error"
        else:
            self.budget += amount
            return self.budget
