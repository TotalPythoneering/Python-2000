# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-12-08 15:30:00
# FILE: ex_assert_none.py
# AUTHOR: Randall Nagy
# ex_assert_none
#

class func():
    value = None        # (1) "class"
    def calc(self):
        self.value = 20 # (2) "instance"
        value = 2       # (3) "local"
        return value
    def getValue(self):
        return self.value

foo = func()
assert(foo.value == None)
print("Local =\t\t", foo.calc())
print("Instance=\t", foo.getValue())
assert(foo.value == 20)  # instance

assert(func.value == None) # Class Unchanged!

