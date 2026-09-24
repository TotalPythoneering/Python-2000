# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_is.py
# AUTHOR: Randall Nagy
# File: ex_is.py
#

zStr = "123"
if zStr is "123":
    print('Okay: Equals str("123")')
if zStr is not 123:
    print("Okay: Not equal int(123)")


class MyClass:
    pass

class YourClass(MyClass):
    pass

print("\nYes - Class : Class")
foo = YourClass
if type(foo) is type(MyClass):
    print("Okay: isa base class!")
    
if type(foo) is type(YourClass):
    print("Okay: isa self, also!")

