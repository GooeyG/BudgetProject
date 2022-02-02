class Budgets():

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"The remaining amount in your {self.name} budget is: £{self.amount}"

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def transfer(self, amount, to, from_):
        self.amount = amount
        self.to = to
        self.from_ = from_

class Food(Budgets):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Bills(Budgets):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Entertainment(Budgets):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount


