import random

a = [0, 0, 0, 0, 1]
b_happens_one = 0
b_happens_two = 0
b_happens_three = 0
b_happens = 0
num = 1000000
for i in range(num):
    a_times = 0
    for k in range(3):
        a_times += random.choice(a)
    if a_times == 3:
        b = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
        b_happens_three += random.choice(b)
        b_happens += random.choice(b)
    elif a_times == 2:
        b = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        b_happens_two += random.choice(b)
        b_happens += random.choice(b)
    elif a_times == 1:
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        b_happens_one += random.choice(b)
        b_happens += random.choice(b)
print("Вероятность происхождения В при трех появлениях А: ", b_happens_three / b_happens)
print("Вероятность происхождения В при двух появлениях А: ", b_happens_two / b_happens)
print("Вероятность происхождения В при одном появлении А: ", b_happens_one / b_happens)
