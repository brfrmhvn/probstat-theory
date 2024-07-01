import random

p1 = random.random()
p2 = random.random()
print("p1 =", p1, "p2 =", p2)
print("Аналитическое решение:", p1 * p2)
good = 0
num = 1000000
for i in range(num):
    a = random.choices([1, 0], weights=[p1, 1 - p1], k=1)[0]
    if a == 1:
        b = random.choices([1, 0], weights=[p2, 1 - p2], k=1)[0]
        if b == 1:
            good += 1
print("Результат моделирования:", good / num)
