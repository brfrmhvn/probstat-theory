import math
import random

l = random.randint(10, 20)
h = random.randint(1, 10)
print(f"Высота h = {h}, длина l = {l}")
print(f"Аналитическое решение: {math.atan(l / h) - h / (2 * l) * math.log(1 + l ** 2 / h ** 2, math.e)}")

num = 1000000
phi = []
for _ in range(num):
    B = random.uniform(0, l)
    phi.append(math.atan(B / h))
print(f"Моделирование: {sum(phi) / num}")
