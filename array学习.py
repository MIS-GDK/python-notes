"""
官方文档：https://docs.python.org/3/library/array.html#array.typecodes
"""

from array import array

a1 = array("i", [11, 11, 22, 13, 16])

print(a1.itemsize)
print(a1.count(11))
print(a1.buffer_info()[1])
a1.append(44)
print(a1.buffer_info()[1])
# print(a1.byteswap())
a1.extend([66, 7, 89])
print(a1, a1.buffer_info()[1])
# a1.frombytes("999")
# print(a1, a1.buffer_info()[1])
a1.fromlist([0, 13, 26])
print(a1, a1.buffer_info()[1])
print(a1.index(13, 3, 9))
print(array(a1.typecode, sorted(a1)))
