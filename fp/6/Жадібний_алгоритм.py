items0 = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
class Item:
    def __init__(self, name,  cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def knapSack(items: list[Item], maxcost: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0

    for item in items:
        if maxcost >= item.cost:
            maxcost -= item.cost
            total_calories += item.calories
            print(item.name)
    return total_calories

names = items0.keys()
items = []
for x in names:
  items.append(Item(x, items0[x]['cost'], items0[x]['calories'])) 



maxCalories = 50
# Виклик функції
print(knapSack(items, maxCalories)) 

