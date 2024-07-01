import random

n = 18
prob = [0, 0, 0, 0, 1]
num = 100000
more_than_three = 0
for i in range(num):
    a = 0
    for k in range(n):
        a += random.choice(prob)
    if a >= 3:
        more_than_three += 1
print(more_than_three / num)
