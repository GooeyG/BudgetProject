from budget import Budgets, Food, Bills, Entertainment

with open("food.txt", "r") as foodVar:
    food_updated = foodVar.read()
with open("ent.txt", "r") as entVar:
    ent_updated = entVar.read()
with open("bills.txt", "r") as billsVar:
    bills_updated = billsVar.read()


JanF = Food("Food", int(food_updated))
JanB = Bills("Bills", int(bills_updated))
JanE = Entertainment("Entertainment", int(ent_updated))

print(JanF, JanB, JanE)




