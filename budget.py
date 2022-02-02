class Budget():

    def __init__(self, balance):
        self.balance = balance


    def __repr__(self):
        return f"The remaining amount in your balance is: £{self.amount} - Reference; '{self.balance}'"

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def transfer(self, amount, to, from_):
        self.amount = amount
        self.to = to
        self.from_ = from_

class Food(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Bills(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Entertainment(Budget):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

Food_b = Food("Food shopping", 500)
Bills_b = Bills("Work clothes", 100)
Ent_b = Entertainment("Bowling", 25)









