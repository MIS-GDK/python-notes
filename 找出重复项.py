from collections import defaultdict, Counter

# 1、利用字典
d1 = defaultdict(list)
"""
with open("C:/Users/Administrator/Desktop/1.txt", "rt", encoding="utf-8") as f:
    line = f.readline().strip()
    while line:
        d1[line].append(0)
        line = f.readline().strip()

for i in d1.keys():
    if len(d1[i]) > 1:
        print(i)
"""
# 使用计数器

list1 = []
with open(r"C:\Users\Administrator\Desktop\1.txt", "rt", encoding="utf-8") as f:
    line = f.readline().strip()
    while line:
        list1.append(line)
        line = f.readline().strip()

c = Counter(list1)
print([k for k in c if c[k] > 1])
