# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_issubclass.py
# AUTHOR: Randall Nagy
# File: ex_issubclass.py
#

class A:
    pass

class B(A):
    pass

if issubclass(A, object) is True:
    print("Okay: A issubclass of object")

if issubclass(object, A) is False:
    print("Okay: object is NOT subclass of A")

print()
try:
    if issubclass(B(), A) is True:
        pass

except TypeError as ex:
    print(ex)

print()
try:
    if issubclass(B, A()) is True:
        pass

except TypeError as ex:
    print(ex)

print()
try:
    if issubclass(A(), A()) is True:
        pass
except TypeError as ex:
    print(ex)
