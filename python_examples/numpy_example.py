# Import namespace convention: np
import numpy as np

# Create an all-zero matrix
#   NOTE: argument is a tuple '(3, 4)'
#     WRONG: np.zeros(3, 4)
#     CORRECT: np.zeros( (3, 4) )
A = np.zeros( (3, 4) )

# numpy creates arrays by default
# CVXPY works best with matrices
# It's best to cast every array to a matrix manually
A = np.asmatrix(A)
print A.shape # size of A

# All-one matrix
B = np.ones( (3, 4) )
B = np.asmatrix(B)

# Identity matrix
I = np.asmatrix(np.eye(5))

# Stacking matrices horizontally
#   Use vstack to stack vertically
J = np.hstack( (I, I) )

# Random matrix with standard Gaussian entries
#   NOTE: argument is NOT a tuple
Q = np.random.randn(4, 4)
Q = np.asmatrix(Q)

print Q
print Q[:, 1] # Second column (everything is 0-indexed)
print Q[2, 3] # (3, 4) entry (as a real number)

# Random column vector of length 4
v = np.asmatrix(np.random.randn(4, 1))

# v.T: v tranpose
z = v.T * Q * v

# The result is a 1-by-1 matrix
print z

# Extract the result as a real number
print z[0, 0]

# Other useful methods
#   Elementwise multiplication
#     np.multiply(A, B)
#   Sum of each column (as a row vector)
#     np.sum(A, axis=0)
#   Sum of each row (as a column vector)
#     np.sum(A, axis=1)

(d, V) = np.linalg.eig(Q) # Eigendecomposition
vnorm = np.linalg.norm(v) # 2-norm of a vector
Qinv = np.linalg.inv(Q) # Matrix inverse
# Solves Qx = v (faster than Qinv*v)
x = np.linalg.solve(Q, v)
