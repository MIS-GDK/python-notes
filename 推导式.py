# data_list = [lambda: 100 for i in range(10)]

# print(data_list)

data_list = [
    lambda x: x + 100,
    lambda x: x + 110,
    lambda x: x + 120,
]


v1 = data_list[0]
print(v1(200))
