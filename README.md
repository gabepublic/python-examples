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

- Useful
```
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
...
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> help(S)
```

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

- docstring
```
>>> import sys
>>> print(sys.__doc__)
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.
```

## EXAMPLES

NOTE: run the examples from the root folder:
```
(.venv) c:\>python file\ex-csv.py 
```

### import
```
import matplotlib.pyplot as plt
from matplotlib import pyplot
```

### For-loop

- range
```
>>> for i in range(10):

>>> list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
([0, 1, 2, 3, 4], [2, 3, 4], [0, 2, 4, 6, 8])
```

- zip
```
>>> L1 = [1,2,3,4]
>>> L2 = [5,6,7,8]
>>> list(zip(L1, L2))
[(1, 5), (2, 6), (3, 7), (4, 8)]

>>> for (x, y) in zip(L1, L2):

>>> keys = ['spam', 'eggs', 'toast']
>>> vals = [1, 3, 5]
dict(zip(keys, vals))
{'eggs': 3, 'toast': 5, 'spam': 1}
```

- enumerate
```
>>> S = 'spam'
>>> E = enumerate(S)
>>> next(E)
(0, 's')
>>> for (offset, item) in enumerate(S):

>>> for (i, line) in enumerate(os.popen('systeminfo')):
```

### Iterator
```
>>> L = [1, 2, 3]
>>> I = iter(L) # Obtain an iterator object from an iterable
>>> I.__next__() # Call iterator's next to advance to next item
1

>>> while True:
...     n = I.__next__()

>>> D = {'a':1, 'b':2, 'c':3}
>>> V = Iter(D.values())
>>> next(V)
1
>>> I = iter(D)
>>> next(I)
'a'
```

### List Comprehension

- basic
```
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
# ~~~~~~~~~~~~~~
# equivalent to
# ~~~~~~~~~~~~~~
squares = []
for x in [1, 2, 3, 4, 5]:
	squares.append(x ** 2)
```

- with condition
```
squares = [x*x for x in [1,2,3,4,5,6] if x <= 5]
```

- nested loop
```
>>> [x + y for x in 'abc' for y in 'lmn']
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```

### Data Structure

- Data structures: tuple, list, set, dictionary 
  - see `datastruc\datastructure.py`
- SORT, see `datastruc\sort-group.py`
- GROUPING, see `datastruc\sort-group.py`

- zip
```
>>> bob1 = dict(name='Bob', job='dev', age=40) # Keywords
>>> bob1
{'age': 40, 'name': 'Bob', 'job': 'dev'}
```

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
__iter__
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

- module reload
```
import changer
[...]
from imp import reload
reload(charger)
[...]
```

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

### Iterators and Generators

- the for loop under the cover; also see "generator" in `ex-iterator.py`
```
for name in names:
	print(name)

>>> equivalent to
it = names.__iter__()
it.__next__()
[...]
```

- simulating linux tail command
```
def follow(filename):
	f = open(filename, 'r')
	f.seek(0, os.SEEK_END)
	while True:
		line = f.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line		# emit the line and makes the function a Generator

for ln in follow('filename'):
	print(ln)
```

### Coroutines

- see `coroutine.py`

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
