class ExLockPrivAttrib():

    def __init__(self, var1):
        # notice _var1 is accessed via the var1 property setter
        self.var1 = var1   

    @property
    def var1(self):
        return self._var1

    @var1.setter
    def var1(self, newvar1):
        if not isinstance(newvar1, int):
            raise TypeError('Expected integer')
        self._var1 = newvar1

if __name__ == '__main__':
    m = ExLockPrivAttrib(5)
    print(m.var1)
    m.var1 = 10
    print(m.var1)
    
    # private attrib is still accessible via dict 
    print(m.__dict__)
    m.__dict__['_var1'] = 20
    print(m.__dict__['_var1'])
    # type error; exception!!!
    err = ExLockPrivAttrib("23")
    