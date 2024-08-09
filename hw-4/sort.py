import random
import timeit


# створення масиву для сортування
n = 10000000
numbers = []
for i in range(n):
    numbers.append(random.randint(0, n))
print(numbers[0])


# сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Сортування вставками (Шелла)
# даний алгоритм змінює сам масив, тому розраховуватиметься останнім
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr






temp = numbers
cod_for_test = """sorted(temp)"""
t3 = timeit.timeit(cod_for_test, number=1, globals=globals())
print(t3, 'вбудована функція')

temp = numbers
cod_for_test = """merge_sort(temp)"""
t1 = timeit.timeit(cod_for_test, number=1, globals=globals())
print(t1, 'Сортування злиттям')

temp = numbers

cod_for_test = """shell_sort(temp)"""
t2 = timeit.timeit(cod_for_test, number=1, globals=globals())
print(t2, 'Сортування вставками (Шелла)')