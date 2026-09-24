# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_class_ref_or_creation.py
# AUTHOR: Randall Nagy
# File: ex_class_ref_or_creation.py
#

class A:
    def __init__(self):
        print("Creating A")

# Simple TYPE reference
zA = A
print(type(zA))

# Creating an instance!
zA = A()
print(type(zA))

## Constructor Chaining
# class B(A):
#     def __init__(self):
#         # A.__init__(self)
#         print("Creating B")
