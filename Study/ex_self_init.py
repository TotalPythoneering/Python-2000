# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-12-08 15:30:00
# FILE: ex_self_init.py
# AUTHOR: Randall Nagy
#


class MyClass:

    def __init__(self, zValue):
        self.value = zValue

    def __init__(self):
        MyClass.__init__("default")


print(MyClass())

print(MyClass("Re-Use!"))





