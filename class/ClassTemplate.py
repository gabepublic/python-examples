# ClassTemplate
#

from abc import ABC, abstractmethod

class ParentClassTemplate():
    # var1 mandatory; var2 optional since it's preset
    def __init__(self, var1):
        self.var1 = var1

    # properties; also protect from setting invalid type
    @property
    def var1(self):
        return self._var1

    @var1.setter
    def var1(self, newvar1):
        if not isinstance(newvar1, int):
            raise TypeError('Expected integer')
        self._var1 = newvar1

    # attribute guard
    def __getattr__(self, name):
        # only called for missing attrib
        #print('ParentClassTemplate getattr : invalid attrib: {}'.format(name))
        raise AttributeError('ParentClassTemplate: invalid attrib: {}'.format(name))

    # enter/exit
    def __enter__(self):
        print('ParentClassTemplate: Entering obj creation')
        return 'some value'

    def __exit__(self, x, y, z):    #TBD why need extra 3 args
        print('ParentClassTemplate: Exiting obj')

    # methods
    @abstractmethod
    def methodA():     # abstract method serves as Design spec
        pass

    def methodB(self):
        print('ParentClassTemplate: methodB')


class ClassTemplate(ParentClassTemplate):

    # var1 mandatory; var2 optional since it's preset
    def __init__(self, var1, var2=0):
        super().__init__(var1)
        self.var2 = var2

    # constructor overloading
    @classmethod
    def set88(cls):
        return cls(88,88)

    # properties; also protect from setting invalid type
    @property
    def var2(self):
        return self._var2

    @var2.setter
    def var2(self, newvar2):
        if not isinstance(newvar2, int):
            raise TypeError('Expected integer')
        self._var2 = newvar2

    # Object Info
    def __repr__(self):
        return 'ClassTempate [var1: {}, var2: {}]' \
            .format(self.var1, self.var2)
	
    def __str__(self):
        return 'ClassTempate (var1, var2): ({}, {})' \
            .format(self.var1, self.var2)

    # methods
    def methodA(self):
        print('ClassTemplate: methodA')

    def methodB(self):
        print('ClassTemplate: methodB')
        super().methodB()


class Typed():
    expected_type = object
    
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Error: expected {}!!'.format(self.expected_type))
        instance.__dict__[self.name] = value

class Integer(Typed):
    expected_type = int


class Point():
    x = Integer('x')
    y = Integer('y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point ({}, {})' \
            .format(self.x, self.y)    


if __name__ == '__main__':
    print('ClassTemplate.mro: ', ClassTemplate.__mro__)
    a = ClassTemplate(1,1)
    print('__dict__ = ', a.__dict__)       # list all the class variables
    print('repr = ', repr(a))
    print('print: ', a)
    print('__mro__ = ', ClassTemplate.__mro__)
    a.methodA()
    a.methodB()
    
    # resource management
    with a as val:
        print('resource management: ', val)

    # demo attrib woth descriptor
    p = Point(8,8)
    print(p)