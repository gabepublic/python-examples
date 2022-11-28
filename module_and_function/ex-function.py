
def greeting(name):
    print('Hello', name)

def helloworld():
    print('Hello World')

import time
def after(seconds, fn):
    print('sleep {} secs...'.format(seconds))
    time.sleep(seconds)
    fn()

def add(x,y):

    def do_add():
        print('{} + {} = {}'.format(x,y,x+y))
        return x+y

    return do_add

def longfunction(x,y,z,d):
    print(x,y,z,d)

def argsfunction (x, *args):
    print(x)
    print(args)

def kwargsfunction (x, **kwargs):
    print(x)
    print(kwargs)


if __name__ == '__main__':
    print('--function is a regular object--------------------')
    greeting('Guido')
    print(greeting)
    g = greeting
    g('Guido')
    print('--function can be passed around--------------------')
    after(1, helloworld)
    after(1, lambda: greeting('Guido after some delay'))
    print('--Lambda is also a function--------------------')
    mylambda = lambda x: x*10
    print(mylambda(5))
    print('--function that makes/returns function--------------------')
    ex_add = add(2,3)
    ex_add()
    print('--function closure--------------------')
    after(1, ex_add)
    print('--function arguments--------------------')
    longfunction(5,6,7,8)
    data = (6,7,8,9)
    longfunction(*data)
    argsfunction(1, 2, 3, 4, 5, 6)
    kwargsfunction(1, a=2, b=3, c=4)
    argsfunction(2, data)