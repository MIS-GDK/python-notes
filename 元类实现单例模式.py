class MyType(type):

    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    # 程序运行到这一步时，__new__已经运行，即对象已经创建，也就是FOO类已经创建
    # 所以运行时这里的cls即 FOO类 <class '__main__.Foo'>
    def __init__(self, name, bases, attrs):
        type.__init__(self, name, bases, attrs)
        self.instance = None

    # 参数cls，代表要实例化的类,这里即是类 <class '__main__.MyType'>
    # 因为是元类,实例化的对象即是 FOO 类，这里的data即为对象 FOO类 <class '__main__.Foo'>
    # 此参数在实例化时由Python解释器自动提供
    def __new__(cls, *args, **kwargs):
        print(cls)
        data = super().__new__(cls, *args, **kwargs)
        return data

    def __call__(self, *args, **kwargs):
        # 1.调用自己那个类的__new__方法去创建对象
        if not self.instance:
            self.instance = self.__new__(self)
        # 2.调用你自己那个类__init__方法去初始化
        self.__init__(self.instance, *args, **kwargs)
        return self.instance


# FOO是一个对象，由MyType创建
# FOO类 是MyType的一个对象
# FOO() -> MyType对象
# 创建类时 会执行MyType的__new__ 和 __init__
class Foo(object, metaclass=MyType):

    def __init__(self, name) -> None:
        self.name = name


# 根据Foo类创建对象，调用MyType.__call__方法
v1 = Foo("alex")
v2 = Foo("gdk")

print(v1)
print(v2)