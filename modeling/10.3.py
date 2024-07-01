import scipy.stats as stats
import matplotlib.pyplot as plt

p = 0.1
k_values = range(1, 6)
probs = []

for k in k_values:
    if k == 5:
        probs.append(stats.geom.pmf(k, p) * 10)
    else:
        probs.append(stats.geom.pmf(k, p))

plt.bar(k_values, probs)
plt.xlabel("Число испытаний до поломки одного из приборов")
plt.ylabel("Вероятность")
plt.title("Ряд распределения числа испытанных приборов")
plt.show()
