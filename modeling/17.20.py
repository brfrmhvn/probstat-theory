import math
import random
import scipy.stats as stats

a = random.randint(0, 10)
R = random.randint(11, 20)
sigma = random.randint(0, 300) / 100
print(f"Сторона куба = {a}, радиус шара = {R}, СКО = {sigma}")
print(
    f"Аналитическое решение: {stats.norm.cdf(R / sigma) - 0.5 - (2 ** (1 / 2) * R / (sigma * math.pi ** (1 / 2)))
                              * math.exp(-R ** 2 / (2 * sigma ** 2)) - (stats.norm.cdf(a / (2 * sigma)) - 0.5) ** 3}")
num = 1000000
good = 0
for _ in range(num):
    x = random.gauss(0, sigma)
    y = random.gauss(0, sigma)
    z = random.gauss(0, sigma)
    if x ** 2 + y ** 2 + z ** 2 <= R ** 2:
        if abs(x) > a / 2 or abs(y) > a / 2 or abs(z) > a / 2:
            good += 1
print(f"Моделирование: {good / num}")
