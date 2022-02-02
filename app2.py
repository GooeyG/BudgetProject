from budget import Budgets, Food, Bills, Entertainment

Food_b = Food("Food", 500)
Bills_b = Bills("Bills", 100)
Ent_b = Entertainment("Entertainment", 25)

food = str(Food_b)
food_int = ''.join(i for i in food if i.isdigit())

bills = str(Bills_b)
bills_int = ''.join(i for i in bills if i.isdigit())

ent = str(Ent_b)
ent_int = ''.join(i for i in ent if i.isdigit())


with open("food.txt", "w") as foodVar:
    foodVar.write(food_int)

with open("bills.txt", "w") as billsVar:
    billsVar.write(bills_int)

with open ("ent.txt", "w") as entVar:
    entVar.write(ent_int)