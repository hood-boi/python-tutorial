#!/usr/bin/env python3
#-EX1-Importing-------------------------------------------------
#Importing Executes the python scripts imported
import dummy1
import dummy1 #Makes no difference : You can't double import. Can only import 1 instance per process

#-EX2-Reloading--------------------------------------------
#from imp import reload <= [This is depricated]
import importlib
import dummy2
importlib.reload(dummy2) #Force Python to run the import again via reload function from imp standard library

#-EX3-Accessing-Module-Attributes------------------------------
from dummy3 import someVariable #Alt: import dummy3
print(someVariable) 		#Alt: dummy3.someVariable

import dummy4
print(dir(dummy4)) #Dir fetches list of name available inside the module ( __X__ are built in names with special meaning to python)

# Module/Namespace is a package of variables names. The names in the package are attributes.
# These 'names' are top level in the package file (basically any global scope names)
# 'names' can be functions, classes, variables and so on

#-EX4-Loading-Multiple-Attributes
from dummy5 import a,b
print(a,b);

#-EX5-Using-exec-to-run-module-files
exec(open('dummy6.py').read());

#-EX6-Overwriting-using-export
to_be_overwitten = "420";
print(to_be_overwitten);
exec(open('dummy7.py').read()); #Exec overwrites your variables
print(to_be_overwitten);
print(to_be_introduced);

#Import introduces a new seperate namespace. Where as exec uses/overwrites the same existing namespace.
