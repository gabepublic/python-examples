# For comparison, see class\ClassTemplate.py

def typed_property(name, expected_type):
    private_name = '_' + name
    
    @property
    def var1(self):
        print(private_name)
        return getattr(self, private_name)

    @var1.setter
    def var1(self, value):
        print(value)
        if not isinstance(value, expected_type):
            raise TypeError('Error: expected {}!!'.format(expected_type))
        setattr(self, private_name, value)

    return var1

Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)
String = lambda name: typed_property(name, str)


class Holding():
    #x = typed_property('x', int)
    #y = typed_property('y', int)
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    h = Holding(1,2)
    print(h.x)
    #h.y = '2'      # uncomment to test wrong type
    
    a = typed_property('a', int)
    a = '5'     # typed_ property only works in Class
    print(a)
    x = Integer('x')
    x = 1
    y = Float('y')
    y = 23.5
    z = String('z')
    z = 'hello'
    q = Integer('q')
    q = '12'
    print('{} {} {} {}'.format(x,y,z,q))