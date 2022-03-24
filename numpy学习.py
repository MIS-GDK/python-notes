import numpy as np

# a = np.array([[1, 2], [3, 3]], dtype=int)

# 设置类型为整数
# y = np.zeros((5,), dtype=int)
# print(y)

y = np.arange(15).reshape(3, 5)
print(y)
print(y.ndim)
print(y.shape)
print(y.dtype)
print(y.itemsize)
