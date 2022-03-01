"""
1.字符串类型(str),在程序中用于表示文字信息,本质上是unicode编码中的二进制

2.字节类型(bytes)
    。可表示文字信息,本质上是utf-8/gbk等编码的二进制(对unicode进行压缩,方便于文件存储和网络传输)
    。可表示原始二进制(图片、文件等信息)
    name = "高鹏远"
    data = name.encode('utf-8')
    result = data.decode('utf-8')
    print(data)
    print(result)
"""
"""
1 读文件
    读取文件，文件不存在时会报错
"""
# 打开文件
file_object = open('info.txt', mode='rt', encoding='utf-8')
# 读取文件
data = file_object.read()
# 关闭文件
file_object.close()
print(data)
"""
2 写文件
    模式:wb(要求写入的文件必须是字节类型)
"""

# file_object = open('t1.txt', mode='wb')

# file_object.write('高鹏远'.encode('utf-8'))

# file_object.close()

# file_object = open('t2.txt', mode='w+', encoding='utf-8')

# file_object.write('高鹏远')

# file_object.close()

import requests

res = requests.get(
    url=
    'https://search.douban.com/movie/subject_search?search_text=%E8%B6%85%E4%BA%BA&cat=1002'
)

file_object = open('log.html', 'wb')
file_object.write(res.content)
file_object.close()
