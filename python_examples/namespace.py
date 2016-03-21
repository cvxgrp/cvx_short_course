# Use the default math module
import math

# Need to use the prefix 'math.' to call functions
# in the math module
print math.factorial(6)

# This imports sin and cos functions only
from math import sin, cos

# No need to use 'math.' prefix for
# individually imported functions
print cos(math.pi/3)

# Use 'rn' namespace for the random module
import random as rn
for i in range(5):
    # print a random number in [0, 1)
    print rn.random()
