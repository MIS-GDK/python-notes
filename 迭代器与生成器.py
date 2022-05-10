# 可迭代对象：如果一个类中有__iter__方法且返回了一个迭代器对象，则这个类创建的对象叫做可迭代对象
# 迭代器：1、类中定义了__iter__和__next__两个方法
#       2、__iter__返回对象本身即self
#       3、__next__方法返回下一个数据，如果没有数据了，则需要抛出一个StopIteration异常
# 生成器：是一种特殊的迭代器

# 基于可迭代对象&迭代器 自定义range

# 迭代器
class IterRange:
    def __init__(self, num):
        self.num = num
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == self.num:
            raise StopIteration
        return self.counter


# 可迭代对象
class Xrange:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        return IterRange(self.max_num)


# obj = Xrange(100)

# for i in obj:
#     print(i)

# 基于生成器版本的 自定义range
class Grange:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        counter = 0
        while counter < self.max_num:
            yield counter
            counter += 1


obj = Grange(20)

for i in obj:
    print(i)
