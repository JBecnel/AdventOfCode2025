from scipy.optimize import milp, Bounds, LinearConstraint
import numpy as np

# Define objective function coefficients
c = np.array([1, 2])

# Define integrality constraints (1 for integer, 0 for continuous)
integrality = np.array([1, 1])

# Define variable bounds
bounds = Bounds([0, 0], [np.inf, np.inf])

# Define linear constraints
A = np.array([[1, 1]])
b_l = np.array([5])
b_u = np.array([5])
constraints = LinearConstraint(A, b_l, b_u)

# Solve the MILP
res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
print(res)