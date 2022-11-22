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

### Game

- https://www.pygame.org/news

### Science

- https://matplotlib.org/

### Web

- https://www.djangoproject.com/


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

### File

- open `csv` file; see `file\ex-csv.py`

### HTTP

- Http request; see `http\ex-urllib.py`

### XML

- Process XML; see `xml\ex-xml.py`

## References

- [1] Python Programming Language; David Beazley; O'Reilly Livelesson
  Published by Addison-Wesley Professional
- [2] Official TUTORIAL - https://docs.python.org/3/tutorial/
- [3] https://pythonspot.com/en/python-flask-tutorials/
- [4] :+1: List of Python books - http://pythonbooks.revolunet.com/
