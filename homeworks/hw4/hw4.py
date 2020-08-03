# Lecture 3 / HOMEWORK 4

# Company
class Company:
    name = ""
    available_shares = 0
    share_price = 0

    def __init__(self, name, shares, price):
        self.name = name
        self.available_shares = shares
        self.share_price = price

    def setSharePrice(self, new_price):
        self.share_price = new_price

    def getSharePrice(self):
        return self.share_price

    def getAvailableShares(self):
        return self.available_shares

    def setShares(self, new_shares):
        self.available_shares = new_shares

    def getName(self):
        return self.name

# Trader class
class Trader:
    name = ""
    budget = 0
    shares = -1

    def __init__(self, name, available_budget):
        self.name = name
        self.budget = available_budget
        self.shares = {}

    def getName(self):
        return self.name

    def getBudget(self):
        return self.available_budget

    def changeBudget(self, new_budget):
        self.budget = new_budget

    def buyShares(self, company, amount):
        # Enough money?
        if self.budget < amount * company.getSharePrice():
            print("Not enough money")
        # Enough shares left?
        elif amount > company.getAvailableShares():
            print("Not enough shares")

        else:
            self.budget -= amount * company.getSharePrice()
            company.setShares(company.getAvailableShares() - amount)
            if company.getName() in self.shares.keys():
                self.shares[company.getName()] += amount
            else:
                self.shares[company.getName()] = amount
            print(amount)

    def sellShares(self, company, amount):
    # The opposite of buyShares, but this time the trader wants to sell shares BACK to the company
    # You need to check if the trader has the number of shares that they want to sell back!
        if company.getName() not in self.shares.keys() or self.shares[company.getName()] < amount:
            print("Not enough shares to sell")
        else:
            self.shares[company.getName()] -= amount
            self.budget += amount * company.getSharePrice()
            company.setShares(company.getAvailableShares() + amount)
            print(amount)

    # For the tradeShares method, we'll need these get/set methods
    def getShares(self):
        return self.shares

    # This one sets EDITS a k/v pair in self.shares
    def setShares(self, k, v):
        self.shares[k] = v

    def tradeShares(self, otherTrader, thisCompany, thisShares, otherCompany, otherShares):
    # This should only be possible if the prices for each set of shares is the same!
    # For example, say j = Joe has 50 shares of a = Apple at $100 a share
    # and b = Bob has 10 shares of g = Google at $200 a share
    # j.tradeShares(b, a, 10, g, 5) is VALID, and the result should be:
    # Joe now has 40 shares of Apple and 5 shares of Google, and
    # Bob now has 10 shares of Apple and 5 shares of Google
    # j.tradeShares(b, a, 10, g, 10) is NOT valid because 10 shares of Apple
    # and 10 shares of Google are NOT the same price!

        # We'll begin with some checks
        this_company_exists = thisCompany.getName() in self.shares.keys()
        other_company_exists = otherCompany.getName() in otherTrader.getShares().keys()
        this_enough_shares = self.shares[thisCompany.getName()] >= thisShares
        other_enough_shares = otherTrader.getShares()[otherCompany.getName()] >= otherShares
        price_equivalent = thisCompany.getSharePrice() * thisShares == otherCompany.getSharePrice() * otherShares

        # If everything is valid
        if this_company_exists and other_company_exists and this_enough_shares and other_enough_shares and price_equivalent:
            self.shares[thisCompany.getName()] -= thisShares
            otherTrader.setShares(otherCompany.getName(), (otherTrader.getShares()[otherCompany.getName()]) - otherShares)
            self.shares[otherCompany.getName()] = self.shares.get(otherCompany.getName(), 0) + otherShares
            otherTrader.setShares(thisCompany.getName(), otherTrader.getShares().get(thisCompany.getName(), 0) + thisShares)
            print("Trade Successful!")
        # Somthing is invalid
        else:
            print("Invalid Request")

# Sample:

# Our companies
google = Company('Google', 100000, 100)
apple = Company('Apple', 200000, 25)
facebook = Company('Facebook', 50000, 10)
amazon = Company('Amazon', 250000, 500)

# Our traders
trump = Trader('Donald Trump', 10000)
biden = Trader('Joe Biden', 5000)
sanders = Trader('Bernie Sanders', 2000)
yang = Trader('Andrew Yang', 4000)

# Sample INVALID operations
trump.buyShares(apple, 500000000)
trump.sellShares(google, 1)

# VALID operations
trump.buyShares(apple, 10)
trump.buyShares(facebook, 50)
biden.buyShares(google, 10)
trump.sellShares(facebook, 20)

# Challenge Problem
sanders.buyShares(apple, 20)
sanders.buyShares(amazon, 1)
yang.buyShares(amazon, 2)
sanders.tradeShares(yang, apple, 21, amazon, 1) # Invalid
sanders.tradeShares(yang, apple, 20, amazon, 1) # Valid
