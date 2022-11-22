# python-examples

Python coding examples.

Python official website: https://www.python.org/

## SETUP

- Install Python
- Install the virtual environment package
- Create virtual environment and activate it
- For instructions, go to https://digitalcompanion.gitbook.io/home/setup/dev-environment/python

### Debugger

Launch the debugger.
```
$ python -i

import pdb;
pdb.set_trace();    # launch debugger
```
[Source: REF-1]


## Python packages

### Web

- https://www.djangoproject.com/

### Game

- https://www.pygame.org/news

### Science

- https://matplotlib.org/


## EXAMPLES

### import
```
import matplotlib.pyplot as plt
```

### For-loop

- range
```
for i in range(10)
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

## References

- [1] Python Programming Language; David Beazley; O'Reilly Livelesson
  Published by Addison-Wesley Professional
- [2] Official TUTORIAL - https://docs.python.org/3/tutorial/
- [3] https://pythonspot.com/en/python-flask-tutorials/
- [4] http://pythonbooks.revolunet.com/
