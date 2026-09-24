#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2019-01-04 13:54:04
# FILE: MyRep.py
# AUTHOR: Randall Nagy
#

class MyRep(int):
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("deletion")
        
    def __new__(self):
        print("new")


# Test
one = MyRep()
two = MyRep()
del two


