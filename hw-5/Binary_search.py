def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 1
 
    while low <= high:
        if(x>arr[high]):
            return (count, -1)
        if (x<arr[low]):
            return (count, -1)
         
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid+1
            # перевірка чи не пропустили значення
            if ((x<arr[low]) & (x>arr[mid])):
                return (count, low)

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid-1
            if ((x>arr[high]) & (x<arr[mid])):
                return (count, high)
         # інакше x присутній на позиції і повертаємо його

        else:
            return (count, mid)
        
        count+=1
 
    # якщо елемент не знайдений
    
    

arr = [2, 3, 4, 10, 40]
x = 6.5
result = binary_search(arr, x)
if result[1] != -1:
    print(f"Element is present at index,  {result[1]}  or his max_limit {arr[result[1]]}")
    print(f"Count = {result[0]}")
else:
    print("Element is not in array borders")