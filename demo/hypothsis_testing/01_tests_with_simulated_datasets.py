# -*- coding: utf-8 -*-
# # Reference
# * [from mosky](https://github.com/YLTsai0609/hypothesis-testing-with-python/blob/master/handouts/04_common_tests.ipynb)

# # Table of Contents
# * 1  Generate a Dataset
# * 2  Compare by Means
# * 3  Compare by Distplots
# * 4  Compare by Boxplots
# * 5  Compare by T-Tests
# * 6  Compare by Confidence Intervals
#

# it's just Mosky's “lab header”
# %matplotlib inline
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import IPython as ip
mpl.style.use('ggplot')
# comment it, or
# download the font from https://www.google.com/get/noto/#sans-hant
# if still fail after install the font, remove the cache dir https://matplotlib.org/faq/troubleshooting_faq.html#matplotlib-configuration-and-cache-directory-locations
# mpl.rc('font', family='Noto Sans CJK TC')
ip.display.set_matplotlib_formats('svg')


np.random.seed(20180701+1)


# # Generate a Dataset

# pd.Series(...) is just like a column in excel
# norm.rvs(loc=mu, scale=sigma, size=n) === sample n from X ~ N(mu, sigma)
# rvs means?
group_ctl = pd.Series(name='height', data=sp.stats.norm.rvs(loc=170, scale=5, size=100))
group_exp_1 = pd.Series(name='height', data=sp.stats.norm.rvs(loc=170, scale=5, size=100))
group_exp_2 = pd.Series(name='height', data=sp.stats.norm.rvs(loc=170+2, scale=5, size=100))

display(group_ctl.head()
,group_exp_1.head(),group_exp_2.head())

# # Compare by Means

group_ctl.describe()

group_exp_1.describe()

group_exp_2.describe()


group_exp_1.mean() > group_ctl.mean()


group_exp_2.mean() > group_ctl.mean()


# # Compare by Displots

sns.distplot(group_ctl)
sns.distplot(group_exp_1)
plt.legend(['Control', 'Experimental 1'])

# +

sns.distplot(group_ctl)
sns.distplot(group_exp_2)
plt.legend(['Control', 'Experimental 2'])
# -

# # Compare by Boxplots

sns.boxplot(data=[group_ctl, group_exp_1, group_exp_2], notch=True)

# * Box: Q1–Q3 = 25th – 75th percentile = 50% of data.
# * Line: the median = the 50th percentile.
# * Whiskers:
#     * Q1 - 1.5 IQR, where IQR = Q3 - Q1.
#     * Q3 + 1.5 IQR.
#     * = 99.3% of data if from a normal distribution.
# * Points: the outliners out of 99.3% of data if from a normal distribution.
# * Notch: 95% confidence interval (CI) of normal distribution.
# * Here the CI comes from Gaussian-based asymptotic approximation with no bootstrap.
# * The CI also can be $ median \pm 1.57\dfrac{IQR}{\sqrt{n}} $.
# * If the notches don't overlap, significant.
#

# # Compare by T-Tests
# * 獨立雙樣本檢定 - two indenpedent samples of scores
#
# [scipy.stats.ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

# alpha: significance level
alpha = 0.05


ttest_result = sp.stats.ttest_ind(group_ctl, group_exp_1)
print(ttest_result)
print(ttest_result.pvalue < alpha)

ttest_result = sp.stats.ttest_ind(group_ctl, group_exp_2)
print(ttest_result)
print(ttest_result.pvalue < alpha)
# 這裡的p值如何解釋呢?
# 重疊的部分面積 - 機率值 : 意即兩抽樣分佈來自同一母體的機率是0.0001
# 小於顯著水平 0.05

# # Put  an Observed Value On

sns.distplot(group_ctl, color='C2')
ov = 177
plt.plot(ov, 0.01, 'p')

# ## Calculate the Probability of the "Tail"

# +
sns.distplot(group_ctl, color='C2')

ax = plt.gca()
kde_x, kde_y = ax.lines[0].get_data()
ax.fill_between(kde_x, kde_y, where=kde_x>ov, alpha=0.5)

# plt.savefig('figures/03_the_tail.png', bbox_inches='tight', dpi=600)

# -

# p-value
#
# = Given the distribution, the probability of more extreme values 
#
# than the observed value.
#
# = P(more extreme values | the distribution)
#
# = P(the tail | the distribution)
#
# = P(X > x | std norm) in this case
#
# The formal definitions:
#
# p-value
#
# = $ P(X \geq x \mid H) $ if right tail event
#
# = $ P(X \leq x \mid H) $ if left tail event
#
# = $ 2\min\{P(X\leq x \mid H),P(X\geq x \mid H)\} $ if double tail event

# +
# TODO : 
# 由data評估出來的kde as a pdf function
# 計算該分佈中大於該資料點的機率
# -







# # Compare by Confidence Intervals

sns.pointplot(data=[group_ctl, group_exp_1, group_exp_2], join=False)


