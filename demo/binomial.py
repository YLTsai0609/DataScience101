"""
    Code by Tae-Hwan Hung(@graykode)
    https://en.wikipedia.org/wiki/Binomial_distribution
"""
import numpy as np
from matplotlib import pyplot as plt

import operator as op
from functools import reduce

def const(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def binomial(n, p):
    q = 1 - p
    y = [const(n, k) * (p ** k) * (q ** (n-k)) for k in range(n)]
    return y, np.mean(y), np.std(y)

for ls in [(0.5, 20), (0.7, 40), (0.5, 40)]:
    p, n_experiment = ls[0], ls[1]
    x = np.arange(n_experiment)
    y, u, s = binomial(n_experiment, p)
    plt.scatter(x, y, label=r'$ p=%.2f, N = %.0f, \mu=%.2f, \sigma=%.2f$' % (p, n_experiment, u, s))


plt.xlabel('$k$ success of experiments')
plt.ylabel('$P(X=k)$ probability')
plt.legend()
plt.show()
# plt.savefig('graph/binomial.png')