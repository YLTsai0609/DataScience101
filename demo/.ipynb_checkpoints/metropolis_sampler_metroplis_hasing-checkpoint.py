# -*- coding: utf-8 -*-
# # Metropolis Sampler
#
# $$p(x) = \left\{
#   \begin{array}{lr}
#     0.2 &  X = 0\\
#     0.8 &  X = 1
#   \end{array}
# \right.$$
#
# 1. `P`為$p(x)$
# 2. `Q`為proposed distribution，$q(x_{t}|x_{t-1})$:
#
# $$
# q(x_{t}=0|x_{t-1}=1) = 1
# $$
# $$
# q(x_{t}=1|x_{t-1}=0) = 1
# $$
#
# 即，位於0時，proposed distribution會"提出"走到1，位於1時會"提出"走到0
#
# 3. 抽樣結果儲存於X
#

# +
import random 
import collections

def metrosamp(iter_counts : int) -> 'List[int]':
    P = {0 : 0.2, 1 : 0.8}
    Q = {1 : 0, 0 : 1}
    X = []
    xt = 0
    for i in range(iter_counts):
        xtp1 = Q[xt] # generate a proposal state from Q
        alpha = min(1., P[xtp1] / P[xt])
        # show the current state, proposal state, and acceptance probability
        # if you want
        print(f'curr :{xt}, proposal {Q[xt]}, acceptance probability {alpha}')
        if random.random() <= alpha:
            xt = xtp1
        X.append(xt)
    return X

def count(X:'List[int]')-> None:
    counter = collections.Counter(X)
    for key in counter:
        print(key, counter[key])


# -

X = metrosamp(100)

# 算一下抽樣的結果是否和預期的機率類似
count(X)

# # Metroplis Hasting
# * Metropolis Hasting也可以用在連續的機率分佈，這裡我們針對gamma distribution來進行抽樣
#
# * 本例實作的gamma distribution抽樣 : 
# $$
# Gamma(x, a, b) = \frac{b^{a}}{\Gamma(a)}x^{a-1}e^{-bx}
# $$
#
# * 抽樣所用的proposed distribution為exponatial distribution : 
# $$
# exp(x, \beta) = \frac{1}{\beta}e^{- \frac{x}{\beta}}
# $$
# * **此例的$q(x)$跟上一個時間點的$x$值無關，即$q(x_{t+1}) = q(x_{t+1}|x_{t})$**
#
#
# 1. 令我們想要抽樣的分佈$a=2$, $b=1$, 程式碼中, `p_func`為$p(x)$
#
# $$
# p(x) = Gamma(x, 2, 1)
# $$
#
#
# 2. 在本例中，令$\beta$ = 5, 程式碼中，`q_func`用於產生$a_{j}$，而`q_func_pdf`用於計算correction factor
#
# $$
# q(x) = exp(x, 5)
# $$
#
# 3. 進行Metropolis Hasting抽樣的演算法為程式碼中的`metrohast`，抽樣結果儲存於`X`。`draw`則是將結果畫成Histogram

# +
import numpy as np
import random 
import collections
import matplotlib.pyplot as plt
import math
import scipy.stats


def p_func_raw(x, a, b):
    S1 = ( (b ** a) / math.gamma(a) )
    S2 = x ** ( a - 1 )
    S3 = math.exp(-b * x)
    return S1 * S2 * S3

def p_func(y):
    return p_func_raw(y, 2, 1)

def q_func(beta):
    return np.random.exponential(beta)

def q_func_pdf(x, beta):
    return scipy.stats.expon.pdf(x, scale=beta)

def metrohast(n_iters):
    X = []
    beta = 5.
    xt = beta
    for i in range(n_iters):
        aj = q_func(beta)
        c = q_func_pdf(xt, beta) / q_func_pdf(aj, beta)
        alpha_original = min(1., (p_func(aj) / p_func(xt)))
        alpha_modified = min(1., (p_func(aj) / p_func(xt)) * c)
        print('-'*60)
        print(f'curr :{xt}, proposal {aj},original alpha {alpha_original}, modified alpha {alpha_modified}, correction factor {c}')
        if random.random() <= alpha_modified:
            xt = aj
        X.append(xt)
    return X
        
def draw(S):
    n, bins, patches = plt.hist(S, 100, normed = 1, facecolor='b', alpha = 0.2)
    plt.plot(bins, [p_func(x) for x in bins], color = 'r')
    plt.show()


# -

X = metrohast(1000)

draw(X)


