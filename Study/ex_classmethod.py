# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_classmethod.py
# AUTHOR: Randall Nagy
# File: ex_classmethod.py
#

class NonInst:
    def __init__(self):
        # instance variable
        self.name = "instance!"

    @classmethod # zClass = "Recipe" 
    def Create(zClass, zName):
        print("@classmethod:",
              type(zClass), "==",
              type(NonInst))
        result = NonInst()
        result.name = zName
        return result

# Class method (factory -w- PARAM)
dual = NonInst.Create("Nagy")
print(dual.name)
