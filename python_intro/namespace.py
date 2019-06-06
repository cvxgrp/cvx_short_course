#!/usr/bin/env python
# coding: utf-8

# # Python namespaces
# 
# This notebook covers the basics of Python namespaces.

# In[1]:


# Use the default math module
import math

# Need to use the prefix 'math.' to call functions in the math module
print(math.factorial(6))


# In[2]:


# This imports sin and cos functions only
from math import sin, cos

# No need to use 'math.' prefix for individually imported functions
print(cos(math.pi/3))


# In[3]:


# Can use custom namespace name different from the module name
# This imports random but uses 'rn' namespace
import random as rn
for i in range(5):
    # print a random number in [0, 1)
    print(rn.random())


# In[4]:


# Import all the 'math' functions into the namespace
# Importing everything without a namespace is generally discouraged
from math import *
print(sin(pi))

