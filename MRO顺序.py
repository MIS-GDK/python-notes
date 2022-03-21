class A:
    def fun(self):
        print("A.fun")


class B(A):
    def fun(self):
        super(B, self).fun()
        print("B.fun")


class C(A):
    def fun(self):
        super(C, self).fun()
        print("C.fun")


class D(B, C):
    def fun(self):
        super(D, self).fun()
        print("D.fun")


# python3 采用C3算法 解析顺序(MRO)
# D类的mro顺序为D->B->C->A,即继承顺序.
D().fun()
print(D.__mro__)
