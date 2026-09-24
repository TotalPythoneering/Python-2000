# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_staticmethod.py
# AUTHOR: Randall Nagy
# File: ex_staticmethod.py
#

class NonInst:
    def __init__(self):
        # instance variable
        self.name = "instance!"

    @staticmethod
    def CreateNamed(name):
        result = NonInst()
        result.name = name
        return result

# Default initializer
dual = NonInst()

# Static method (factory -w- PARAM)
dual = NonInst.CreateNamed("Nagy")
print(NonInst.name, dual.name)

