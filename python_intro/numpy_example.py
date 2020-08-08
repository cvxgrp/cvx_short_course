#!/usr/bin/env python
# coding: utf-8

# # NumPy
# 
# This notebook covers the basics of NumPy, the Python matrix library.

# In[1]:


# NumPy namespace convention: np
import numpy as np

# Create an all-zero matrix
#   NOTE: argument is a tuple '(3, 4)'
#     WRONG: np.zeros(3, 4)
#     CORRECT: np.zeros( (3, 4) )
A = np.zeros((3, 4))


print(A)
print(A.shape) # dimensions of A


# In[2]:


# All-one matrix
B = np.ones((3, 4))
print(B)

# Identity matrix
I = np.eye(5)
print(I)

# Stacking matrices horizontally
#   Use vstack to stack vertically
J = np.hstack((I, I))
print(J)


# In[3]:


# Random matrix with standard Gaussian entries
#   NOTE: argument is NOT a tuple
Q = np.random.randn(4, 4)

print(Q)
print(Q[:, 1]) # Second column (everything is 0-indexed)
print(Q[2, 3]) # (3, 4) entry (as a real number)


# In[4]:


# Random column vector of length 4
v = np.random.randn(4, 1)

# v.T: v tranpose
# @: matrix multiplication
z = v.T @ Q @ v

# The result is a 1-by-1 matrix
print(z)

# Extract the result as a real number
print(z[0, 0])


# In[5]:


# Other useful methods
#   Construct a matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 3.2], [5, 8]])
#   Transpose a matrix
print(A.T)
#   Elementwise multiplication
print(np.multiply(A, B))
#   Sum of each column (as a row vector)
print(np.sum(A, axis=0))
#   Sum of each row (as a column vector)
print(np.sum(A, axis=1))


# In[6]:


# Linear algebra routines
Q = A.T @ A
(d, V) = np.linalg.eig(Q) # Eigen decomposition
print("d = ", d)
print("V = ", V)

v = np.array([1, 2])
print("||v||_2 = ", np.linalg.norm(v)) # 2-norm of a vector

Qinv = np.linalg.inv(Q) # Matrix inverse
# Solves Qx = v (faster than Qinv*v)
x = np.linalg.solve(Q, v)
print("Q^{-1}v = ", x)

