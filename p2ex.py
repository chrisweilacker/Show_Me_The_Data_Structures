## Locally save and call this file ex.py ##
s
# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./p2ex.py"))

# Does the file end with .py?
print ("./p2ex.py".endswith(".py"))