import random
import math


def calc_sum(x, y):
    result = 0
    for j in range(x - y):
        result += (-1) ** j / math.factorial(j)
    return result


n = random.randint(10, 200)
m = random.randint(1, 10)
print("n =", n, "m =", m)
print("Аналитическое решение:", (1 / math.factorial(m)) * calc_sum(n, m))
num = 1000000
good = 0
seats = list(range(1, n + 1))
for i in range(num):
    correct = 0
    tickets = seats[:]
    random.shuffle(tickets)
    for k in range(n):
        if seats[k] == tickets[k]:
            correct += 1
    if correct == m:
        good += 1
print("Результат моделирования:", good / num)
