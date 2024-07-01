import random

box = ["red", "black", "white"]
num = 100000
two_or_more = 0
for i in range(num):
    result = []
    for k in range(5):
        result.append(random.choice(box))
    if result.count("black") >= 2 and result.count("white") >= 2:
        two_or_more += 1
print(two_or_more / num)
