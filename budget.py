class Budget():

    def __init__(self, ref):
        self.ref = ref


    def __repr__(self):
        return f"The remaining amount in your balance is: {self.amount} - Reference; '{self.ref}'"

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

food = str(Food_b)
food_int = ''.join(i for i in food if i.isdigit())
print(food_int)

bills = str(Bills_b)
bills_int = ''.join(i for i in bills if i.isdigit())
print(bills_int)

ent = str(Ent_b)
ent_int = ''.join(i for i in ent if i.isdigit())
print(ent_int)

with open("food.txt", "w") as foodVar:
    foodVar.write(food_int)

with open("bills.txt", "w") as billsVar:
    billsVar.write(bills_int)

with open ("ent.txt", "w") as entVar:
    entVar.write(ent_int)
