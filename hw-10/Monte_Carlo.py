# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Khcq4BVPS6YPJweLFXW5FTf9cD-PbDKD
"""

import random

import scipy.integrate as spi

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, "Похибка: ", error)

# Розміри прямокутника
a = 2  # ширина прямокутника
b = 4  # висота прямокутника

def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) під параболою."""
    return y <= x**2

# Генерація випадкових точок
def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(1500000)]
        # Відбір точок, що знаходяться під параболою
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area



# Кількість експериментів
num_experiments = 100

# Виконання симуляції
average_area = monte_carlo_simulation(a, b, num_experiments)

print(f"Середня площа під параболою із {num_experiments} експериментів: {average_area}")