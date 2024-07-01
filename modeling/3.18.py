import math
import random

L = random.randint(1, 1000)
d = random.randint(0, L)
v1 = random.randint(1, L)
v2 = random.randint(1, L)
print("L =", L, "v1 =", v1, "v2 =", v2, "d =", d)
print("Аналитическое решение:", 1 - (1 - d / L * math.sqrt(1 + (v2 / v1) ** 2)) ** 2)
good = 0
num = 1000000
for i in range(num):
    x = random.randint(0, L)
    y = random.randint(0, L)
    if abs(x - y) <= d * math.sqrt(1 + (v2 / v1) ** 2):
        good += 1
print("Результат моделирования:", good / num)
