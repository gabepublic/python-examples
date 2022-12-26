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
Source: [REF-1](#references)

## Utilities

- **Code formatter**:
  - The PEP 8 (Python Enhancement Proposal) document at 
    https://www.python.org/dev/peps/pep-0008/ describes best practices 
    for formatting code that most editors will automatically format
  - YAPF (Yet Another Python Formatter, https://github.com/google/yapf)
  - Black (https://github.com/psf/black)

- **Code Linter**, report problems in the code, such as declaring a 
  variable but never using it:
  - Pylint - https://www.pylint.org/
  - Flake8 - http://flake8.pycqa.org/en/latest/
  - Mypy tool http://mypy-lang.org/ find problems, such as using text
   when you should be using a number

## Python packages

### Python standard packages
Doc: https://docs.python.org/3/library/index.html

| Module | Description |
| -------| ----------- |
| datetime | Defines classes to store and perform calculations using date and time values |
| tempfile | Defines a range of functions to work with temporary files and directories |
| csv | Supports reading and writing of CSV format files |
| hashlib | Implements cryptographically secure hashes |
| logging | Allows you to write log messages and manage log files |
| threading | Supports multi-threaded programming |
| html | A collection of modules (that is, a package) used to parse and generate HTML documents |
| unittest | A framework for creating and running unit tests |
| urllib | A collection of modules to read data from URLs |

### Extension packages
- Date & Time:
  - The dateutil package (https://github.com/dateutil/dateutil) extends
    the datetime package included in the Python Standard Library, adding
    support for recurring dates, time zones, complex relative dates, etc.
- Game
  - https://www.pygame.org/news
- Science
  - https://matplotlib.org/
- Web
  - https://www.djangoproject.com/
- Graphics
  - Python Imaging Library (PIL); PIL is no longer being actively
    developed; http://python-pillow.org/
- PDF
  - ReportLab is a commercial PDF generator, which is also released 
    under an open source license. http://www.reportlab.com/opensource/.
- XML
  - The `lxml` toolkit (http://lxml.de) takes the pain out of reading
    and writing XML- and HTML-formatted documents
- Testing
  - `unittest`
  - the coverage package (https://pypi.python.org/pypi/coverage).
  - the `unittest.mock` package in the Python Standard Library

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

## TEST

- Install `pytest`
```
$ pip install pytest
$ pytest --version

$ pytest -v test.py
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
- Use a tool such as Sphinx (http://www.sphinx-doc.org) to convert the 
  docstrings into API documentation for the package.

## EXAMPLES - fundamental
- First line of the python file, let OS find the python interpreter 
  to use on the linux environment:
```
#!/usr/bin/env python3
```
- NOTE: run the examples from the root folder:
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

### Python magic method (`__xx__`)
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
- see [`module_and_function\README.md`](https://github.com/gabepublic/python-examples/tree/main/module_and_function)
  for discussions & examples
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

### Decorator
- Very good source: https://realpython.com/primer-on-python-decorators/
- In python, it’s possible to define functions inside other functions.
  Such functions are called inner functions.
```
def parent():
  print("parent")

  def first_child():
    print("first_child")
  
  first_child()
```
OUTPUT:
```
>>> parent()
parent
first_child
```

- A decorator is a design pattern in Python that allows a user to add 
  new functionality to an existing object without modifying its 
  structure. Decorators are usually called before the definition of 
  a function you want to decorate.

- Example of decorator. Decorators wrap a function, modifying its behavior.
```
def reponse_to_mailman(func):
  def wrapper():
    print("a mailman is approaching")
    func()

def bark():
  print("woof")
```
OUTPUT:
```
>>> response = reponse_to_mailman(bark)
>>> response()
a mailman is approaching
woof
```

- Example decorator with `@` declaration symbol, and function with
  arguments
```
def reponse_to_mailman(func):
  def wrapper(*args, **kwargs):
    print("a mailman is approaching")
    func(*args, **kwargs)
  return wrapper
  
@reponse_to_mailman
def bark():
  print("woof")

@reponse_to_mailman
def make_sound(sound):
  print(sound * 2)
```
OUTPUT:
```
>>> make_sound("woof")
>>> bark()
a mailman is approaching
woofwoof
a mailman is approaching
woof
```

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

- Generator is also useful for preventing memory issue due to loading
  very large file, as shown below. Assume a very large `sample.txt`
  file exists.
```
def read_file(filename):
  #data =[]
  with open(filename, "r") as input_file:
    for line in input_file:
      # data.append(line)
      yield line

contents = read_file("sample.txt")

# shorter syntax to replace read_file function
contents_1 = (line for line in open("sample.txt", "r"))

for line in contents:
  print(line)
```

### Context Manager
- Without context manager, file is not closed when `file.write` 
  encounters exception:
```
file = open('hello.txt', 'w')
file.write('Hello, World')
file.close()
```
- Using try-catch to address the issue:
```
file = open('hello.txt', 'w')
try:
  file.write('Hello, World')
except Exception as e:
  print('error: ', e)
finally:
  file.close()
```
- Using context manager
```
with open('hello.txt', mode='w') as f:
  file.write('Hello, World')
```
- How python does it; using context manager protocol:
  - `__enter__()` which, if it returns something, becomes the target of
    the `as` portion of the statement, and a `__exit__()` method that is
    called when the context block goes out of scope

### Coroutines
- see `coroutine.py`

### HTTP
- Http request; see `http\ex-urllib.py`
- JSON; see `datastruc\datastructure.py`

### XML
- Process XML; see `xml\ex-xml.py`

## Modular Programming
Source: Modular Programming with Python by Erik Westra; O'Reilly;
Published by Packt Publishing; [Github](https://github.com/packtpublishing/modular-programming-with-python)
Also see above: 
- [Examples - Modules & Packages](#modules--functions)
- [Python packages](#python-packages)

- Python provides two constructs to facilitate modular programming: 
  modules and packages.
  - module is the most basic method; module can be built-in, or written
    in Python, or C. A “python” file (i.e., contains python codes and 
    has py filename extension is a module
  - package is a grouping of modules in a folder such that it can be 
    referenced using dot notation to avoid module names collision.

- Python package is distributed in the form of archived file (.whl). 
  The wheel file is uploaded to repository, Python Package Index and 
  other indexes, to share with others.
  - `pip` is the recommended “package installer” for python.

- To Package Python, see [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-your-project-to-pypi)

- Import:
  - If you are importing from a **module**, all of the top-level functions, 
    constants, classes, and other definitions will be imported. 
  - When importing from a **package**, all of the top-level functions,
    constants, and so on defined in the package's `__init__.py` file 
    will be imported.
  - Controlling what objects from the module or package gets imported
    using the `__all__` variable as shown below. If the package has
    `module_3`, it will not get imported.
```
__all__ = ["module_1", "module_2", "sub_package"]
```
   - WATCHOUT for circular dependency.
```
# module_1.py
from module_2 import calc_markup
def calc_total(items):
...
    calc_markup(10)

# module_2.py

from module_1 import calc_total
def calc_markup(total):
    return total * 0.1
def make_sale(items):
    total_price = calc_total(items)
    ...

# error
# ImportError: cannot import name calc_total
```

- EXTENSIBLE module using dynamic import
```
from importlib import import_module

# module name is provided from input
module_name = input("Load module: ")
if module_name != "":
    module = importlib.import_module(module_name)
    module.say_hello()
```
  - PLUGIN pattern: you can set up a separate directory, let say at the
    top level of your program, to place the plugins, or you could store
    your plugins in a directory outside of your program's source code,
    and modify `sys.path` so that the Python interpreter can find the 
    modules in that directory.
  - HOOKS pattern: allowing external code to be called at particular 
    points in your program
```
# package_1
login_hook = None

def set_login_hook(hook):
    login_hook = hook

def login(username, password):
...
  if login_hook != None:
      login_hook(username)

# the application
def my_login_hook(username):
  print('the hook function...')
  ...

login_module.set_login_hook(my_login_hook)
```  

- The **module search path** is stored in `sys.path`, and the Python 
  interpreter will check the directories in this list one after another
  until the desired module or package is found. When the Python 
  interpreter starts, it initializes the module search path with the 
  following directories:
  - The directory containing the currently-executing script, or 
  - the current directory if you are running the Python interactive 
    interpreter in a terminal window
  - Any directories listed in the PYTHONPATH environment variable
  - The contents of the interpreter's site-packages directory, 
    including any modules referred to by path configuration files 
    within the site-packages directory
  - A number of directories containing the various modules and packages
    that make up the Python Standard Library
```
>>> import sys
>>> print(sys.path)
['', '/usr/local/lib/python3.3/site-packages', 
'/Library/Frameworks/SQLite3.framework/Versions/B/Python/3.3', 
'/Library/Python/3.3/site-packages/numpy-override', 
'/Library/Python/3.3/site-packages/pip-1.5.6-py3.3.egg', 
'/usr/local/lib/python3.3.zip', '/usr/local/lib/python3.3', 
'/usr/local/lib/python3.3/plat-darwin', 
'/usr/local/lib/python3.3/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3', 
'/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin']
>>>
>>> sys.path.append("/usr/local/shared-python-libs")
>>>
>>> sys.path.insert(1, "/usr/local/shared-python-libs")   # move up the module search priority
```
**Notice** that we use insert(1, ...) rather than insert(0, ...)

## Book - Tiny Python Projects

Tiny Python Projects; by Ken Youens-Clark
Published by Manning Publications; O'Reilly
Github: https://github.com/kyclark/tiny_python_projects

### FastAPI

- install FastAPI package
```
$ pip install fastapi
$ pip install uvicorn
```
- See Github [gabepublic/api-fastapi-py-basic](https://github.com/gabepublic/api-fastapi-py-basic)
- NOTE: fastapi uses python Decorator 


## Misc notes
- function placeholder using `pass`
```
def set_locations(locations):
    pass
``` 

## Python conventions
- Python Style Guide (https://www.python.org/dev/peps/pep-0008/) that 
  provides a clear set of recommendations for how to format and style 
  your code.
- Module naming using all lowercase letters, and underscore if needed. 
  Refer to https://www.python.org/dev/peps/pep-0008/#package-and-module-names
  for more details.

## References
- [1] Python Programming Language; David Beazley; O'Reilly Livelesson
  Published by Addison-Wesley Professional
- [2] Official TUTORIAL - https://docs.python.org/3/tutorial/
- [3] https://pythonspot.com/en/python-flask-tutorials/
- [4] :+1: List of Python books - http://pythonbooks.revolunet.com/
- [5] https://www.blog.pythonlibrary.org/
