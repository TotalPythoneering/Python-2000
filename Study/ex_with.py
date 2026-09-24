# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_with.py
# AUTHOR: Randall Nagy
# File: ex_with.py
#

## A context manager can create a new object-context

## whenever using 'with':
# https://www.python.org/dev/peps/pep-0343/

class foo():
    def __init__(self):
        self.zname = "init.name"

    def __enter__(self): # with block
        self.zname = "with.enter.name"

    def __exit__(self, xtype, xval, trace):
        self.zname = "with.exit.name"

    def name(self):
        return self.zname


# Justanobject ...
bla = foo()

# Consistent block entry / exit values 
print("pre:\t", bla.name())       # normal

if(True):
    print("block:\t", bla.name()) # normal
# Activate __enter__ via "with"
try:
    with bla:
        print("with:\t", bla.name())# enter block
    print("xblock:\t", bla.name())  # exit block
finally:
    print("finally:", bla.name())   # exit block
print("(post:\t", bla.name(), "still!")

class MyConMgr():
    def __enter__(self):
        pass
    def __exit__(self, xtype, xval, trace):
        pass       

zTest = MyConMgr()
