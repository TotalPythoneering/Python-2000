# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ex_globals_and_locals.py
# AUTHOR: Randall Nagy
#
print("\n", type(globals()))

if globals() is locals():
    print("\nfirst.both\n",locals())

def foo():
    snarfblat = 0
    print("\nfoo.globals\n",globals())
    print("\nfoo.locals\n",locals())

foo()

if globals() is locals():
    print("\nlast.both\n",locals())



