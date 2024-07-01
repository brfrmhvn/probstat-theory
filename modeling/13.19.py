import random
from scipy.stats import moment, t

n = random.randint(1, 50)
k = random.randint(1, n % 10 + 1)
if k % 2 == 0:
    v = k // 2
    m_k = 1
    for i in range(1, 2 * v, 2):
        m_k *= i
    for i in range(2, 2 * v + 1, 2):
        m_k /= n - i
    m_k *= n ** v
else:
    m_k = 0
print(f"Степени свободы: {n}, порядок: {k}, аналитическое значение момента: {m_k}")
num = 1000000
moment_k = 0
for i in range(num):
    data = t.rvs(n, size=100)
    moment_k += moment(data, k)
print(f"Моделирование: {moment_k / num}")
