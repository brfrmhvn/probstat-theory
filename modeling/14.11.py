import numpy as np

mean = 10
sigma = 30
n = 1000000
good = 0
for i in range(n):
    x1 = np.random.normal(mean, sigma)
    x2 = np.random.normal(mean, sigma)
    if x1 > 10 and x2 < -10 or x1 < -10 and x2 > 10:
        good += 1

print(good / n)
