# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_nonlocal.py
# AUTHOR: Randall Nagy
#
def func():
       value = 1
       def calc():
           # How to re-use above?
           value = 2
           print("calc:", value)
       calc()
       print("func:", value)

func()

def func():
       value = 1
       def calc():
           nonlocal value
           value = 2
           print("calc:", value)
       calc()
       print("func:", value)

func()
