import numpy as np

# a = np.array([[1, 2], [3, 3]], dtype=int)
"""
# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)
"""

"""
y = np.arange(15).reshape(3, 5) 
print(y)
print(y.ndim) 数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank。
print(y.shape) 数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)。因此，shape 元组的长度就是rank或维度的个数 ndim。
print(y.dtype) 一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外NumPy提供它自己的类型。例如numpy.int32、numpy.int16和numpy.float64。
print(y.itemsize) 数组中每个元素的字节大小。例如，元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）。它等于 ndarray.dtype.itemsize 
"""
"""
# 花式索引
# 使用索引数组进行索引
a = np.arange(12) ** 2  # the first 12 square numbers
print(a)  # an array of indices
i = np.array([1, 1, 3, 8, 5])  # the elements of a at the positions i
print(a[i])

j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print(a[j])  # the same shape as j

# 当索引数组a是多维的时，单个索引数组指的是第一个维度a。以下示例通过使用调色板将标签图像转换为彩色图像来显示此行为。
palette = np.array(
    [
        [0, 0, 0],  # black
        [255, 0, 0],  # red
        [0, 255, 0],  # green
        [0, 0, 255],  # blue
        [255, 255, 255],  # white
    ]
)

image = np.array(
    [[0, 1, 2, 0], [0, 3, 4, 0]]  # each value corresponds to a color in the palette
)

print(palette[image])

# 可以为多个维度提供索引。每个维度的索引数组必须具有相同的形状。
a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1], [1, 2]])  # indices for the first dim of a
j = np.array([[2, 1], [3, 3]])  # indices for the second dim
print(a[i, j])  # i and j must have equal shape
# array([[ 2,  5],
#        [ 7, 11]])
"""

# 使用数组索引的另一个常见用法是搜索与时间相关的系列的最大值：
time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
print(time)
print(data)
ind = data.argmax(axis=0)
print(ind)
# print(time[ind])
data_max = data[ind, range(data.shape[1])]
print(data_max)
print(range(data.shape[1]))
