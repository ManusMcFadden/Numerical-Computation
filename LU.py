import numpy as np
A = np.array([[-1, 2, 1], [4, 0, 2], [3, 2, -5]], dtype=float)
L = np.identity(3, dtype=float)
U = np.zeros((3, 3), dtype=float)

for i in range(3):
    for j in range(i, 3):
        uSum = 0
        for k in range(i):
            uSum += L[i, k] * U[k, j]
        U[i, j] = A[i, j] - uSum

    for j in range(i + 1, 3):
        lSum = 0
        for k in range(i):
            lSum += L[j, k] * U[k, i]
        L[j, i] = (A[j, i] - lSum) / U[i, i]

print(L)
print(U)
