import numpy as np

A = [[1, 4, 5],
     [-5, 8, 9],
     [6, 8, 10],
     [0, 2, 38]]
print("A = ", A)
print("A[1] =", A[1])
print("A[1][2] =", A[1][2])
print("A[0][-1] =", A[0][-1])

a = np.array([[1, 4, 5], [-5, 8, 9], [6, 8, 10], [0, 2, 38]])
print("type:", type(a))
print("a =", "\n", a, "\n")
print("a[1] =", a[1])
print("a[1][2] = ", a[1][2])
print("a[0][-1] =", a[0][-1])

c = np.array([[1, 1, 2], [3, 5, 3], [5, 6, 9]])
c[:, 2]

s = sum(c[:])
print(s)
a = sum(c)
print(a)
