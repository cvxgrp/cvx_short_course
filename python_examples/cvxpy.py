from cvxpy import *
import numpy as np

# Problem data.
m = 30
n = 20
np.random.seed(1)
A = np.asmatrix(np.random.randn(m, n))
b = np.asmatrix(np.random.randn(m,1))

# Construct the problem.
x = Variable(n)
# Operator overloading of * and -.
cost = sum_squares(A*x - b)
objective = Minimize(cost)
# Constructing a list.
# Operator overloading of <=.
constraints = [0 <= x, x <= 1]
prob = Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
# The optimal value for x is stored in x.value.
print x.value
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print constraints[0].dual_value
