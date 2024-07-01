import math
import random


def xj(n):
    array = []
    for _ in range(10):
        array.append(random.binomialvariate(1, p))
    return sum(array)


p = random.random()
q = 1 - p
print(f"p = {p}, q = {1 - p}")
y = []
py = []
for i in range(1, 11):
    py.append(round(math.comb(10, i) * p ** i * q ** (10 - i), 6))
print(f"Ряд, полученный аналитически: {py}")

num = 1000000
Py = [0] * 10
for _ in range(num):
    y = xj(10)
    for i in range(1, 11):
        if y == i:
            Py[i - 1] += 1
Py = [x / num for x in Py]
print(f"Моделирование: {Py}")
