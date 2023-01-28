Q1: How to use pip to remove an installed package?
1) pip --uninstall package
2) pip install --uninstall package
3) pip remove package
4) pip uninstall package [X]

Q2: The pyc file contains: 
1) compiled Python code [X]
2) Python source code
3) a Python interpreter
4) a Python interpreter

Q3: The pip list command presents a list of:
1) locally installed packages [X]
2) available pip commands
3) outdated local packages
4) all packages available at PyPI

Q4: What is TRUE about the pip install command ? (Select two answers)
1) it allows the user to install a specific version of the package [X]
2) it always installs the newest package version and it cannot be changed
3) it installs a package system-wide only when the --system option is specified
4) it installs a package per user only when the --user option is specified [X]

Q5: Chose the TRUE statement (Select two answers)
1) The system function from the platform module returns a string with your OS name [X]
2) The version function from the platform module returns a string with your Python version
3) The version function from the platform module returns a string with your OS version [X]
4) The processor function from the platform module returns an integer with the number of processes currently running in your OS

Q6: During the first import of a module, Python deploys the pyc files in the directory called:
1) hashbags
2) \__pycache\__ [X]
3) mymodules
4) \__init\__

Q7: A predefined Python variable that stores the current module name is called:
1) __module__
2) __modname__
3) __mod__
4) __name__ [X]

Q8: A function which returns a list of all entities available in a module is called:
1) entities()
2) content()
3) dir() [X]
4) listmodule()

Q9: The digraph written as #!! is used to:
1) create a docstring
2) make a particular module entity a private one
3) tell a Unix or Unix-like OS how to execute the contents of a Python file [X] 
4) tell an MS Windows OS how to execute the contents of a Python file

Q10: Knowing that a function named fun() resides in a module named mod, and it has been imported using the following line:
import mod
Choose the way it can be invoked in your code: 
1) mod:: fun()
2) fun()
3) mod.fun() [X]
4) mod->fun()

Q11: When a module is imported, its contents:
1) are ignored
2) may be executed (explicitly)
3) are executed once (implicitly) [X]
4) are executed as many times as they are imported

Q12: A list of package's dependencies can be obtained from pip using its command name:
1) deps
2) list
3) show [X]
4) dir

Q13: The following statement 
from a.b import c
causes the import of 
1) entity a from module b from package c
2) entity c from module a from package b
3) entity b from module a from package c
4) entity c from module b from package a [X]

Q14: What is TRUE about updating already installed Python packages?
1) it can be done only by uninstalling and installing the packages once again
2) it can be done by reinstalling the package using the reinstall command
3) it's performed by the install command accompanied by the -U option [X]
4) it's an automatic process which doesn't require any user attention

Q15: Knowing that a function named fun() resides in a module named mod, choose the correct way to import it:
1) from mod import fun [X]
2) from fun import mod
3) import fun from mod
4) import fun

Q16: What is true about the pip search command ? (Select three answers)
1) all its searches are limited to locally installed packages
2) it needs working internet connection to work [X]
3) it searches through all PyPI packages [X]
4) it searches through package names only [X]

Q17: What is the expected value of the result variable after the following code is executed?
import math
result = math.e != math.pow(2, 4)
print(int(result))
1) False
2) 1 [X]
3) 0
4) True

Q18: What is the expected output of the following code?
from random import randint

for i in range(2):
print(randint(1, 2), end=' ') 

1) 11, 12, 21, or 22 [X]
2) 12, or 21
3) 12
4) there are millions of possible combinations, and the exact output cannot be predicted