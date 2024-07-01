from random import random
import numpy as np
from scipy.stats import norm

mean = random()
sigma_x = random()
x = np.random.normal(mean, sigma_x)
fx = norm.pdf(x)
print(fx)

