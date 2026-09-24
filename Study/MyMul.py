#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2019-01-04 12:26:42
# FILE: MyMul.py
# AUTHOR: Randall Nagy
#

class MyMul:

    def __init__(self):
        self._val = 0

    def assign(self, str_value):
        try:
            self._val = int(str_value)
        except:
            self._val = 0
        return self._val

    def __imul__(self, ival):
        print("ival:", type(ival))
        self._val = self._val * ival
        return self # Important!
    
    def __mul__(self, dval):
        print("dval:", type(dval))
        return self._val * dval


x = MyMul()
x.assign("2")
print(x * 10)
print(x * 10.10)
x *= 7
print(x._val)



