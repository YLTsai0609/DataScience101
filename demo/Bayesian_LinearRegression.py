# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# Ref
# https://github.com/WillKoehrsen/Data-Analysis/blob/master/bayesian_lr/Bayesian%20Linear%20Regression%20Demonstration.ipynb
# Pandas and numpy for data manipulation
import pandas as pd
import numpy as np

# Matplotlib and seaborn for visualization
import matplotlib.pyplot as plt
# %matplotlib inline 

import seaborn as sns

# Linear Regression to verify implementation
from sklearn.linear_model import LinearRegression

# Scipy for statistics
import scipy

# PyMC3 for Bayesian Inference
import pymc3 as pm


# +
exercise = pd.read_csv('data/exercise.txt')
calories = pd.read_csv('data/calories.txt')

df = pd.merge(exercise, calories, on = 'User_ID')
df = df[df['Calories'] < 300]
df = df.reset_index()
df['Intercept'] = 1
df.head()


# +
plt.figure(figsize=(8, 8))

plt.plot(df['Duration'], df['Calories'], 'bo');
plt.xlabel('Duration (min)', size = 18); plt.ylabel('Calories', size = 18); 
plt.title('Calories burned vs Duration of Exercise', size = 20);
# -

# Create the features and response
X = df.loc[:, ['Intercept', 'Duration']]
y = df.ix[:, 'Calories']


# Takes a matrix of features (with intercept as first column) 
# and response vector and calculates linear regression coefficients
def linear_regression(X, y):
    # Equation for linear regression coefficients
    beta = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y)
    return beta


# # Run the by hand implementation
# by_hand_coefs = linear_regression(X, y)
# print('Intercept calculated by hand:', by_hand_coefs[0])
# print('Slope calculated by hand: ', by_hand_coefs[1])


#  Create the model and fit on the data
# lr = LinearRegression()
# lr.fit(X.Duration.reshape(-1, 1), y)
# print('Intercept from library:', lr.intercept_)
# print('Slope from library:', lr.coef_[0])


# # PyMC3 for Bayesian inference
# * rather than a single point estimated of model weighrs, Bayesian linear regression will give us a posterior distribution for the model weights

# 慢, 跟linear regression比起來, 真, 慢
with pm.Model() as linear_model_500:
    # pick our prior distribution of our parameters
    # Intercept
    intercept = pm.Normal('Intercept', mu=0, sd=10)
    
    # Slope
    slope = pm.Normal('slope', mu = 0, sd = 10)
    
    # Stand devairation
    sigma = pm.HalfNormal('sigma', sd = 10)
    
    # Edstimate of mean
    mean = intercept + slope * X.loc[0:499, 'Duration']
    
    # Observed values
    Y_obs = pm.Normal('Y_obs', mu = mean, sd = sigma, observed = y.values[0:500])
    
    # Sampler 
    step = pm.NUTS()
    
    # Posterior distribution
    linear_model_500 = pm.sample(1000, step)
    
