import numpy as np

J = np.random.normal(10, 0.1, 1000000)
R = np.random.normal(30, 0.2, 1000000)
T = np.random.normal(600, 0.5, 1000000)

Q = 0.24 * J ** 2 * R * T

print(np.var(Q) ** (1 / 2))
