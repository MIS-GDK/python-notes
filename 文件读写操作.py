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