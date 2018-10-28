class A:
    def go(self):
        print('A')
class B(A):
    def go(self):
        print('B')
        super().go()
class C(A):
    def go(self):
        print('C')
        super().go()

class D(B,C):
    def go(self):
        print('D')
        super(self.__class__,self).go()
d=D()
print(D.__mro__)
d.go()

