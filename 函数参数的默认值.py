"""
def func(a1,a2=18):
   print(a1,a2)
python在创建函数（未执行）时，如果发现函数的参数中有默认值，则在函数内部会创建一块区域并维护这个默认值
执行函数未传值时，则让a2指向函数维护的那个值的地址
   func('alex')
执行函数传值时，则让a2指向新传入的值的地址
   func('admin',12)
"""

"""
在特定情况下 [默认参数的值是可变类型] & [函数内部会修改这个值]下,参数的默认值 需要特别注意
"""

# 1
# def func(a1, a2=[1, 2]):
#     a2.append(666)
#     print(a1, a2)


# func(100)
# func(200)
# func(99, [77, 88])
# func(300)

# 2


# def func(a1, a2=[1, 2]):
#     a2.append(a1)
#     return a2


# v1 = func(10)
# print(v1)
# v2 = func(20)
# print(v2)
# v3 = func(30, [11, 22])
# print(v3)
# v4 = func(40)
# print(v4)

# 3
def func(a1, a2=[1, 2]):
    a2.append(a1)
    return a2


v1 = func(10)
v2 = func(20)
v3 = func(30, [11, 22])
v4 = func(40)

print(v1)
print(v2)
print(v3)
print(v4)