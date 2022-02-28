text1 = "我是{0},今年{1}岁,我的真实名字是{0}".format("高鹏远", 18)
print(text1)

text2 = "我是{n1},今年{n2}岁,我的真实名字是{n1}".format(n1="高鹏远", n2=18)
print(text2)

text3 = "我是{n1},今年{n2}岁,我的真实名字是{n1}"
print(text3.format(n1='高鹏远', n2=18))

action = '跑步'

text4 = f"我是高鹏远,我非常喜欢{action}"
print(text4)

name = "文静"
age = 18
text5 = f'女朋友的名字叫{name},她今年{18+2}岁'
print(text5)