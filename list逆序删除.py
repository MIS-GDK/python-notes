list1 = [1, 2, 4, 5, 6, 7]
# 从后往前删除 避免 list index out of range
print(list1[:2])

for i in range(len(list1) - 1, -1, -1):
    print(i, list1[i])
    del list1[i]

print(list1)
