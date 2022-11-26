class ExClass():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    @classmethod
    def set88(cls):
        return cls(88,88)
    
    def getVar1(self):
        return self.var1

# Inheritance: abstractmethod, add childvar
# Multiple inheritance:  
from abc import ABC, abstractmethod
class Parent():
    @abstractmethod
    def tobeimpemented():     # abstract method serves as Design spec
        pass

    def spam(self):
        print("Parent.spam")

class A(Parent):
    def __init__(self, childvar):    # new constructor & add childvar
        self.childvar = childvar
        super().__init__()    # MUST initialize parent

    def tobeimpemented():
        print("A.tobeimpemented")
    
    def spam(self):
        print("A.spam")
        super().spam()

class ImplParent(Parent):
    def tobeimpemented():
        print("ImplParent.tobeimpemented")

class B(A):
    def tobeimpemented():
        print("B.tobeimpemented")

    def spam(self):
        print("B.spam")
        super().spam()

class C(ImplParent):
    def spam(self):
        print("C.spam")
        super().spam()

class D(ImplParent):
    def spam(self):
        print("D.spam")
        super().spam()

class E(C, D):
    def spam(self):
        print("E.spam")
        super().spam()

if __name__ == '__main__':
    # Inheritance
    c = ExClass.set88()
    print("ExClass var1: ", c.getVar1())

    # Multiple inheritance
    x = 4
    a = A(x)
    a.spam()

    b = B(x)
    b.spam()
    
    e = E()
    print("E.mro: ", E.__mro__)
    e.spam()
