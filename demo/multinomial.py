"""
    Code by Tae-Hwan Hung(@graykode)
    https://en.wikipedia.org/wiki/Multinomial_distribution
    3-Class Example
"""
import numpy as np
from matplotlib import pyplot as plt

import operator as op
from functools import reduce

def factorial(n):
    return reduce(op.mul, range(1, n + 1), 1)

def const(n, a, b, c):
    """
        return n! / a! b! c!, where a+b+c == n
        這裏只考慮的排列數，而沒有加入每個category的機率，因此output並分一個機率分佈
    """
    assert  a + b + c == n

    numer = factorial(n)
    denom = factorial(a) * factorial(b) * factorial(c)
    return numer / denom

def multinomial(n):
    """
    :param x : list, sum(x) should be `n`
    :param n : number of trial
    :param p: list, sum(p) should be `1`
    """
    # get all a,b,c where a+b+c == n, a<b<c
    # i,j,k,指的是發生事件的次數when n = 20, (i,j,k) = (1,1,18), (2,1,17),...
    # 組合ls總共33種可能，接著再輸入const這個function
    # 這裡忽略了(0,0,20)的可能性, 都從1開始
    ls = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if i + j + k == n:
                    ls.append([i, j, k])

    y = [const(n, l[0], l[1], l[2]) for l in ls]
    x = np.arange(len(y))
    return x, y, np.mean(y), np.std(y)

for n_experiment in [20, 21, 22]:
    x, y, u, s = multinomial(n_experiment)
    plt.scatter(x, y, label=r'$trial=%d$' % (n_experiment))

plt.legend()
# plt.xlabel('k-th combination')
plt.ylabel('Numbers of combination')
plt.show()
plt.savefig('graph/multinomial.png')