# -*- coding: utf-8 -*-
import cvxpy as cp
import numpy as np

print("Starting optimization problem...")

# Problem data.
m = 30
n = 20
print(f"Problem dimensions: m={m}, n={n}")
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

# Construct the problem.
x = cp.Variable(n)
objective = cp.Minimize(cp.sum_squares(A @ x - b))
constraints = [0 <= x, x <= 1]
prob = cp.Problem(objective, constraints)

# The optimal objective value is returned by `prob.solve()`.
print("Solving the optimization problem...")
result = prob.solve()
print(f"Optimal objective value: {result}")
print(f"Problem status: {prob.status}")

# The optimal value for x is stored in `x.value`.
print("\nOptimal value for x:")
print(x.value)

# The optimal Lagrange multiplier for a constraint is stored in
# `constraint.dual_value`.
print("\nDual values for constraints:")
print(f"First constraint (0 <= x): {constraints[0].dual_value}")
print(f"Second constraint (x <= 1): {constraints[1].dual_value}")

print("\nOptimization completed successfully!")
