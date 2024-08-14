import timeit

def find_coins_greedy(total):
    coin =[50, 25, 10, 5, 2, 1] # номінали
    count = {}
    for i in range (len(coin)):
        x= total//coin[i]
        if x>0:
            count[coin[i]] = x
            total = total - x*coin[i]
    return count
print(find_coins_greedy(6))



def minCoinChange(change):
   coinVal = [50, 25, 10, 5, 2, 1]
   minCoins = [0]*(change+1)
   coinsUsed = [0]*(change+1)
   count = []
   
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1

      for j in coinVal:
        if j > cents:
            continue

        if minCoins[cents-j] + 1 < coinCount:
            coinCount = minCoins[cents-j]+1
            newCoin = j
            
    
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   coin = change
   
   
   while coin > 0:
      
      thisCoin = coinsUsed[coin]
      
      count.append(thisCoin)             
      coin = coin - thisCoin
   coinList = {}   
   
   
   for k in range(len(count)):
       if count[k] not in coinList:
        coinList[count[k]] = 1
                 
       else:
            coinList[count[k]] = coinList[count[k]] + 1
       
       
       
   
   
   return coinList

print(minCoinChange(6))

cod_for_test = """find_coins_greedy(6)"""   
t1 = timeit.timeit(cod_for_test, number=1, globals=globals())
print(t1, 'Жадібний алгоритм')

cod_for_test = """minCoinChange(6)"""   
t2 = timeit.timeit(cod_for_test, number=1, globals=globals())
print(t2, 'Динамічний алгоритм')
