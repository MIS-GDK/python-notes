from collections import defaultdict
import operator

d1 = defaultdict(list)
d2 = defaultdict(list)
with open(r"C:\Users\Administrator\Desktop\1.txt") as f:
    line = f.readline().strip()
    while line:
        id, col = line.split()
        d1[id].append(col)
        line = f.readline().strip()

with open(r"C:\Users\Administrator\Desktop\2.txt") as f:
    line = f.readline().strip()
    while line:
        id, col = line.split()
        d2[id].append(col)
        line = f.readline().strip()

for i in set(d1.keys()) | set(d2.keys()):
    if not operator.eq(sorted(d1[i]), sorted(d2[i])):
        # 集合异或操作
        # print(i,set(d1[i])^set(d2[i]))
        # 只存在于d1中的方法如下
        # symmetric_difference 返回两个集合中不重复的元素集合。
        comp = set(d1[i]).symmetric_difference(d2[i])
        # 只存在的d1中的
        if [x for x in d1[i] + d2[i] if x in comp and x in d1[i]]:
            print(
                "存在于正式环境的"
                + i
                + ":%s" % [x for x in d1[i] + d2[i] if x in comp and x in d1[i]]
            )
        # # 只存在的d2中的
        # if [x for x in d1[i] + d2[i] if x in comp and x in d2[i]]:
        #     print(
        #         "存在于测试环境的"
        #         + i
        #         + ":%s" % [x for x in d1[i] + d2[i] if x in comp and x in d2[i]]
        #     )


for i in set(d1.keys()) | set(d2.keys()):
    if not operator.eq(sorted(d1[i]), sorted(d2[i])):
        # 集合异或操作
        # print(i,set(d1[i])^set(d2[i]))
        # 只存在于d1中的方法如下
        # symmetric_difference 返回两个集合中不重复的元素集合。
        comp = set(d1[i]).symmetric_difference(d2[i])
        # 只存在的d1中的
        # if [x for x in d1[i] + d2[i] if x in comp and x in d1[i]]:
        #     print(
        #         "存在于正式环境的"
        #         + i
        #         + ":%s" % [x for x in d1[i] + d2[i] if x in comp and x in d1[i]]
        #     )
        # 只存在的d2中的
        if [x for x in d1[i] + d2[i] if x in comp and x in d2[i]]:
            print(
                "存在于测试环境的"
                + i
                + ":%s" % [x for x in d1[i] + d2[i] if x in comp and x in d2[i]]
            )
