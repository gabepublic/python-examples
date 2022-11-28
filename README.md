# python-examples

Python coding examples.

Python official website: https://www.python.org/

## SETUP

- Install Python
- Install the virtual environment package
- Create virtual environment and activate it
- For instructions, go to https://digitalcompanion.gitbook.io/home/setup/dev-environment/python

### Debugger

Launch the debugger in "interactive" mode when the program crash.
This allow introspection of the variable
```
$ python -i test.py
>>>
>>> print(p)
```

Alternatively, add the launch debugger in the code nearby to the
suspected issue code. The program will stop at that line enabling 
further debugging.
``` 
import pdb; pdb.set_trace();    # launch debugger
```
[Source: REF-1]


## Python packages

- Game
  - https://www.pygame.org/news

- Science
  - https://matplotlib.org/

- Web
  - https://www.djangoproject.com/


## REPL

- Enter REPL
```
$ python
>>> 
```
-  Python path
```
# example in the virtual environment
>>> import sys
>>> sys.path
['', 'C:\\zApps\\Python311\\python311.zip', 'C:\\zApps\\Python311\\DLLs', 'C:\\zApps\\Python311\\Lib', 'C:\\zApps\\Python311', 'C:\\zCodes\\python-examples\\.venv', 'C:\\zCodes\\python-examples\\.venv\\Lib\\site-packages']
>>> 
```
  - better approach is setting the `PYTHONPATH`

## Documentation

Documentation shows up using `help(sample.add)
- function
```
# sample.py
def add(x,y):
	'''
	Add x and y
	'''
```

## EXAMPLES

NOTE: run the examples from the root folder:
```
(.venv) c:\>python file\ex-csv.py 
```

### import
```
import matplotlib.pyplot as plt
```

### For-loop

- range
```
for i in range(10):
```

### Comprehension
```
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
# ~~~~~~~~~~~~~~
# equivalent to
# ~~~~~~~~~~~~~~
squares = []
for x in [1, 2, 3, 4, 5]:
	squares.append(x ** 2)
```

### Data Structure

- Data structures: tuple, list, set, dictionary 
  - see `datastruc\datastructure.py`
- SORT, see `datastruc\sort-group.py`
- GROUPING, see `datastruc\sort-group.py`

## Python magic method (`__xx__)

- Operators
```
>>> x + 10		# equivalent tyo x.__add__(10)
>>> names = ['one', 'two', 'three']
>>> names[0]    # equiv to names.__getitem__(0)
```

- Usage with Python class
```
class Point():
	def __add__(self, other):
		[...]

>>> p = Point(0,0)
>>> p + 10
```

- Printable & Debug friendly; NOTE: should add to all class created
```
class Point():
	def __repr__(self):
		return "Point({!r}, {!r})", self.x, self.y)
	
	def __str__(self):
		return "Point coordinate (x,y): ({}, {})"

>>> p = Point()
>>> p			# will call __repr__
>>> repr(p)		# will call __repr__
>>> print(p)	# will call __str__
>>> str(p)	    # will call __str__
```

- For custom containers use the magic methods align with Python styles,
  examples:
```
__class__
__name__
__dict__		# holding all the class & object attributes
__len__
__getitem__
__iter__
__enter__		# similar to onEnter; enable to use with [..] as [..]:
__exit__		# similar to onExit; enable with [..] as [..]:
__getattribute__
__setattribute__
__getattrib__	# will be called for missing attribute 
__getattrib__
[...]
```

### File

- open `csv` file; see `file\ex-csv.py`

### Modules & Functions

- see `module_and_function\README.md` for discussions & examples
- see `module_and_function\simple.py`
- see `module_and_function\ex-function.py`

### Lambda Function

- Simple example of lambda function; see `datastruc\sort-group.py`
- Also see examples in `module_and_function` folder

### Class

- For Summary of good practice, see `class\ClassTemplate.py`

- NOTE: class name does not take "-"
```
File "c:\zCodes\python-examples\class\ex-class.py", line 1
    class ex-class(object):
            ^
SyntaxError: invalid syntax
```

- Python does not prevent adding attribute to the object on the fly.
  See `var3` is added to the object even though `ExClass` does not have
  the attribute `var3`. This could be a PROBLEM!
```
(.venv) c:\zCodes\python-examples>python -i class\ExClass.py
>>> myclass = ExClass(10,20)
>>> myclass.var1
10
>>> myclass.var2
20
>>> myclass.getVar1()
10
>>> myclass.var3 = 80
>>> myclass.var3
80
>>>
```

- **NOTE:** by convention, all variables with `_`, for example, `_var1`
  should be treated as private variable of that class 

- `getattr` and `setattr` method
```
>>> >>> myclass.var1
10
>>> getattr(myclass, 'var1')
10
>>>
```

- Interesting feature of the class method call
```
# involves two steps: getting the method and calling the method
>>> myclass.getVar1()
# So, is EQUIVALENT to the following
>>> (myclass.getVar1)()
# or the following
>>> c = myclass.getVar1
>>> c()
>>>
```

- OVERRIDING the class constructor; see `class\ExClass.py`
```
    @classmethod
    def set88(cls):
```

- Inheritance; see `class\ExClass.py`
- Multiple Inheritance; see `class\ExClass.py`
- Method resolution object, `__mro__`; see `class\ExClass.py`
- Locking private attribute;  see `class\ExLockPrivAttrib.py`

- Type check
```
def print(formatter):
	if not isintance(formatter, BaseFormatter):
		raise TypeError("formatter must be a BaseFormatter")
```

### Metaclass


### HTTP

- Http request; see `http\ex-urllib.py`
- JSON; see `datastruc\datastructure.py`

### XML

- Process XML; see `xml\ex-xml.py`

## References

- [1] Python Programming Language; David Beazley; O'Reilly Livelesson
  Published by Addison-Wesley Professional
- [2] Official TUTORIAL - https://docs.python.org/3/tutorial/
- [3] https://pythonspot.com/en/python-flask-tutorials/
- [4] :+1: List of Python books - http://pythonbooks.revolunet.com/
