#!/usr/bin/env python3
import dummy1
import dummy1 #Makes no difference : You can't double import. Can only import 1 instance per process

from imp import reload
import dummy2
reload(dummy2) #Force Python to run the import again via reload function from imp standard library 
