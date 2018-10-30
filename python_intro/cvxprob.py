import cvxpy as cvx
import numpy as np

# Problem data.
m = 30
n = 20
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

# Construct the problem.
x = cvx.Variable(n)
# *, +, -, / are overloaded to construct CVXPY objects.
cost = cvx.sum_squares(A*x - b)
objective = cvx.Minimize(cost)
# <=, >=, == are overloaded to construct CVXPY constraints.
constraints = [0 <= x, x <= 1]
prob = Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
# The optimal value for x is stored in x.value.
print(x.value)
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print(constraints[0].dual_value)
