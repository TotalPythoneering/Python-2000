# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_isinstance.py
# AUTHOR: Randall Nagy
# File: ex_isinstance.py
#

class A:
    pass

class B(A):
    pass

class C(object):
    pass

zA = A()
zB = B()
zC = C()

if isinstance(zA, object) is True:
    print("Okay: zA isinstance of object")

if isinstance(zA, C) is False:
    print("Okay: zA isinstance NOT of C")

if isinstance(zA, B) is False:
    print("Okay: zA isinstance NOT of B")

if isinstance(zC, (A, B)) is False:
    print("Okay: zC isinstance NOT of A or B!")

print()
try:
    if isinstance(zB, zA) is True:
        pass
        # print("Error: zB isinstance of zA?")

except TypeError as ex:
    print(ex)

