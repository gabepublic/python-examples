# Python Module and Function

## MODULE

Python file, `*.py`, is a module.

### `simple.py`

- Running
```
(.venv) $ python simple.py
running simple.py...
fn: run...
x is  88

(.venv) $
```

### Using REPL to explore `simple.py`

- Enter REPL
```
(.venv) $ cd module
(.venv) $ python
>>>
```

- import `simple` module; 
  - **NOTE:**
    - python cache the module; a subsequent import will be silent, as 
      shown below
  	- when `simple.py` is modified, exit REPL and re-enter before
      changes can take effect.
```
>>> import simple
running simple.py...
fn: run...
x is  88
>>> simple
<module 'simple' from 'c:\\zCodes\\python-examples\\module\\simple.py'>
>>>  simple.x
88
>>> simple.spam()
x is  88
>>> simple.run()
fn: run...
x is  88
>>> import simple		# second import
>>>
>>> quit()
(.venv) $
```

- import `simple.run` only; only `run` is visible not others; but
  the entire module is loaded. Calling `spam()` will fail but calling
  `run()` will call `spam()` and it will work. 
```
(.venv) $ cd module
(.venv) $ python
>>> from simple import run
running simple.py...
fn: run...
x is  88
>>> spam()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> run()
fn: run...
x is  88
>>>
```

- starting REPL from the parent folder of the module
```
(.venv) $ ls
module
(.venv) $ python
>>> import simple
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'simple'
>>> import module.simple
running simple.py...
fn: run...
x is  88
>>>
```

- To make `simple.py` a module, refactor slightly:
```
if __name__ == '__main__':
	print("running simple.py...")
	run()
```


### Create a package

- create a package directory, `mypckg`

- package files
```
__init__.py
simple.py
main.py[...etc...]
```

- Initialization code can be added to `__init__.py`

- to import the `simple.py` module from the `main.py`
```
import mypckg.simple

# BETTER approach
from . import simple
```

## FUNCTION

Python function is just a regular Python object

- see `ex-function.py`
- function can make function; see `ex-function.py`
- function that takes any number of arguments

## FUNCTION - Lambda

- Lambda function; see `ex-function.py`

## FUNCTION - Closure

Exploring further the above example about the "function makes function",
see `ex-function.py`, the `def add(x,y)` function captures & stores
the x & y and returns it with the function; this is the Python Closure.
So, even when x & y are deleted after the "function return", the
return function still works, and remembers x & y.

Closure is useful for:
- for create & prepare a function to be executed at later point in time

- see `ex-closure.py`

## Decorator

- for example adding logging to all the functions; see `ex-decorator.py`