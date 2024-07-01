import random
import statistics

m = random.randint(1, 1000)
n = random.randint(1, 1000)
print("m =", m, "n = ", n)
print("Аналитическое решение: M[X] =", n / m, "D[X] =", n * (m + n) / m ** 2)
num = 1000000
black_num = []
box = [0, 1]
for i in range(num):
    ball = 1
    black = 0
    while ball == 1:
        ball = random.choices(box, weights=[m, n], k=1)[0]
        if ball == 1:
            black += 1
    black_num.append(black)
print("Моделирование: M[X] =", statistics.mean(black_num), "D[X] =", statistics.variance(black_num))
