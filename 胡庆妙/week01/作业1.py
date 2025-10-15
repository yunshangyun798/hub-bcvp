import torch

import numpy as np

# 创建两个矩阵
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("矩阵 A:")
print(A)
print("\n矩阵 B:")
print(B)

# 矩阵乘法
print("\n矩阵乘法结果 np.dot(A,B):")
print(np.dot(A, B))


# 或者使用 @ 运算符（Python 3.5+）
print("\n矩阵乘法结果 (@ 运算符):")
print(A @ B)




a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(X)
print(a + X)
print((a * X).shape)

print(a + A)
