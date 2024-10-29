import numpy as np

# create arrays of float values
matrix = np.array([[2, -4, 2], [-5, 1, 4], [-5, 1, 3]], dtype=float)
vector = np.array([3, -3, 0], dtype=float)
unknown = np.zeros(len(vector), dtype=float)

# gaussian elimination
for i in range(len(vector) - 1):
    for j in range(i + 1, len(vector)):
        multValue = (-matrix[j, i] / matrix[i, i])
        matrix[j] += multValue * matrix[i]
        vector[j] += multValue * vector[i]

# backwards substitution
for k in reversed(range(len(vector))):
    if k == len(vector) - 1:
        unknown[k] = vector[k] / matrix[k, k]
    else:
        sum = 0
        for m in range(k + 1, len(vector)):
            sum += matrix[k, m] * unknown[m]
        unknown[k] = (vector[k] - sum) / matrix[k, k]

# print [x1, x2, x3]
print(unknown)
