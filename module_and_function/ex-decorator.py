# ex-decorator.py
# decorator

from functools import wraps
def logged(func):
    print('Adding logging to ', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Calling', func.__name__)
        print(args)
        print(kwargs)
        return  func(*args, **kwargs)

    #wrapper.__name__ = func.__name__
    #wrapper.__doc__ = func.__doc__

    return wrapper

def logformat(fmt):

    def logged(func):
        print('Adding logging formatted to ', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            print(args)
            print(kwargs)
            return  func(*args, **kwargs)

        return wrapper

    return logged
    
@logged
def add(x,y):
    '''
    Add x and y
    '''
    return x+y
#add = logged(add)      # decorate with @logged

loggedformatted = logformat('LOG formatted: Calling {func.__name__}')

@loggedformatted
def mul(x,y):
    '''
    Multiply x and y
    '''
    return x*y
#mul = logged(mul)

@loggedformatted
def sub(x,y):
    '''
    Subtract y from x
    '''
    return x-y

if __name__ == '__main__':
    print('result:', add(2,3))
    print('result:', mul(2,3))
    print('result:', sub(10,3))