import heapq

def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]

# Масив для сортування
arr = [30, 11, 45, 7, 20, 19]
sorted_arr = heap_sort(arr)
print("Відсортовані довжини кабелів:", sorted_arr)




