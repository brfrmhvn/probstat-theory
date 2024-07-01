import math
import scipy.stats as stats
import numpy as np

y = 0.5
a = 2

print(f"a) Плотность вероятности СВ Y = {1 / (3 * math.pi * (1 + (1 - y) ** (2 / 3))) * (1 - y) ** (1 / y)}")
print(f"b) Плотность вероятности СВ Y = {a ** (1 / 2 / (math.pi * (a + y) * y ** (1 / 2)))} (a = {a})")
print(f"b) Плотность вероятности СВ Y = {-a ** (1 / 2 / (math.pi * (a + y) * y ** (1 / 2)))} (a = {-a})")
print(f"c) Плотность вероятности СВ Y = {1 / math.pi}")
print(f"d) Плотность вероятности СВ Y = {1 / (math.pi * (1 + y ** 2))}")

X = stats.cauchy.rvs(0, 1, size=1000000)
Y = np.array([
    1 - X ** 3,
    2 * X ** 2,
    np.arctan(X),
    1 / X])


# Функция для оценки плотности вероятности с помощью гистограммы
def pd(data, value, bins=10):
    hist, edges = np.histogram(data, bins=bins, density=True)
    bin_index = np.searchsorted(edges, value) - 1
    return hist[bin_index]


print(f"a) Моделирование: {pd(Y[0], y, bins=50)}")
print(f"b) Моделирование: {pd(Y[1], y, bins=50)}")
print(f"c) Моделирование: {pd(Y[2], y, bins=50)}")
print(f"d) Моделирование: {pd(Y[3], y, bins=50)}")
