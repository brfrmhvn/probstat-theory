import random

lamps = 1000
takenLamps = 100
all_good = 0
num = 100000
for k in range(100000):
    i = random.randint(0, 5)  # случайный выбор кол-ва испорченных лампочек
    lamps_list = ['bad'] * i + ['good'] * (lamps - i)
    selected_lamps = random.sample(lamps_list, takenLamps)
    if 'bad' not in selected_lamps:
        all_good += 1
prob = all_good / num
print(prob)
