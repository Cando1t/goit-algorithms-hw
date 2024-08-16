items0 = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def get_cost_and_calories(food):
  names = food.keys()
  cost = []
  calories = []
  for x in names:
    cost.append(food[x]['cost'])

    calories.append(food[x]['calories'])
      
  return cost, calories

def get_memtable(food, A):
      cost, calories = get_cost_and_calories(food)
      n = len(calories) # розміри таблиці
    
      # таблиця з нулями
      V = [[0 for a in range(A+1)] for i in range(n+1)]
      
      for i in range(n+1):
            for a in range(A+1):
                  # базовий випадок
                  if i == 0 or a == 0:
                        V[i][a] = 0

                  # якщо ціна менше лишених коштів
                  # максималізуємо сумарну калорійність
                  elif cost[i-1] <= a:
                        V[i][a] = max(calories[i-1] + V[i-1][a-cost[i-1]], V[i-1][a])

                  # якщо ціна більше лишених коштів
                  # беремо значення з попередньої строки
                  else:
                        V[i][a] = V[i-1][a]
             
      return V, cost, calories

def get_selected_items_list(food, A):
        V, cost, calories = get_memtable(food, A)
        n = len(calories)
        res = V[n][A]      # починаємо з останнього елементу таблиці
        a = A              # залишених коштів максимум
        items_list = []    # список цін та калорійностей
        print(res) # максимальна калорійність
        
    
        for i in range(n, 0, -1):  #в зворотьому напрямку
            if res <= 0:  # умова обриву - склали  "рюкзак" 
                  break
            if res == V[i-1][a]:  # йдемо далі
                  continue
            else:
                  # купуємо їжу
                  items_list.append((cost[i-1], calories[i-1]))
                  res -= calories[i-1]   
                  a -= cost[i-1] 
       

        selected_food = []
       

      # ннази харчів
      
        for search in items_list:
            for y in food.keys():
               if ((food[y]['cost'] == search[0])):
                      selected_food.append(y)
            
        return selected_food

f = get_selected_items_list(items0, 50)
print(f)
