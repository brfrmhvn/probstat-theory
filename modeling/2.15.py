import random
import math

n = random.randint(1, 100)
m = random.randint(1, 100)
k = random.randint(1, n + m)
s = random.randint(1, m)
while s > k or s > n:
    s = random.randint(1, m)
print("n =", n, "m =", m, "k =", k, "s =", s)
print("Аналитическое решение:", (math.comb(n, s) * math.comb(m, k - s)) / math.comb(n + m, k))
good = 0
num = 1000000
for i in range(num):
    tickets = n * [1] + m * [0]
    chosen = 0
    for j in range(k):
        if random.choice(tickets) == 0:
            tickets.remove(0)
        else:
            tickets.remove(1)
            chosen += 1
    if chosen == s:
        good += 1
print("Результат моделирования:", good / num)