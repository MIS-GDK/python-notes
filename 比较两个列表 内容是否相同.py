import operator

list1 = [
    "华润河南医药有限公司新稀特大药房",
    "0103263",
    "化学药品",
    "托伐普坦片",
    "瑞贝坦",
    "片剂",
    "15mg*10片*1板",
    "15mg*10片*1板",
    "盒",
    99999,
    99999,
    "国内(除港澳台)",
    "945HN",
    "江苏恒瑞医药股份有限公司",
    None,
    None,
    "国药准字H20213152",
    None,
    None,
    "遮光，密封，30℃以下保存。",
    1080,
    None,
    13,
    13,
    None,
]
list2 = [
    "华润河南医药有限公司新稀特大药房",
    "0103263",
    "化学药品",
    "托伐普坦片",
    "瑞贝坦",
    "片剂",
    "15mg*10片*1板",
    "15mg*10片*1板",
    "盒",
    99999,
    99999,
    "国内(除港澳台)",
    "945HN",
    "江苏恒瑞医药股份有限公司",
    None,
    None,
    "国药准字H20213152",
    None,
    None,
    "遮光，密封，30℃以下保存。",
    1080,
    None,
    13,
    13,
    None,
]


print(operator.eq(list1, list2))
