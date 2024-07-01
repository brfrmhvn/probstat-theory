import random
import scipy.stats as stats

alpha = random.randint(1, 10)
x0 = random.randint(1, 10)
print(f"Альфа = {alpha}, x0 = {x0}")
print(f"Аналитическое решение: x* = {2 ** (1 / alpha) * x0}")
num = 1000000
good = []

for _ in range(num):
    x_rand = stats.pareto.rvs(alpha, loc=0, scale=x0, size=1, random_state=None)[0]
    prob = 1 - (x0 / x_rand) ** alpha
    if round(prob, 3) == 0.500:
        good.append(x_rand)
print(f"Моделирование: x* = {sum(good) / len(good)}")
