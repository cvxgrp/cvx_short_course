#!/usr/bin/env python
# coding: utf-8

# # CVXPY
# 
# This Python notebook shows a basic example using CVXPY.

# In[2]:


import cvxpy as cp
import numpy as np


# Problem data.
m = 10
n = 7
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

# Construct the problem.
x = cp.Variable(n)
# *, +, -, / are overloaded to construct CVXPY objects.
cost = cp.sum_squares(A*x - b)
objective = cp.Minimize(cost)
# <=, >=, == are overloaded to construct CVXPY constraints.
constraints = [0 <= x, x <= 1]
prob = cp.Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
# The optimal value for x is stored in x.value.
print(x.value)
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print(constraints[0].dual_value)

