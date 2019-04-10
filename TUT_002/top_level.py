#!/usr/bin/env python3
#Importing Executes the python scripts imported
import dummy1
import dummy1 #Makes no difference : You can't double import. Can only import 1 instance per process

from imp import reload
import dummy2
reload(dummy2) #Force Python to run the import again via reload function from imp standard library

from dummy3 import someVariable #Alt: import dummy3
print(someVariable) 		#Alt: dummy3.someVariable

import dummy4
print(dir(dummy4)) #Dir fetches list of name available inside the module ( __X__ are built in names with special meaning to python)
