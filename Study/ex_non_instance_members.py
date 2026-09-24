# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-12-08 15:30:00
# FILE: ex_non_instance_members.py
# AUTHOR: Randall Nagy
# File: ex_non_instance_members.py
#

class NonInst:
    # class variable - common to all!
    name = "class_var"
    
    def __init__(self):
        # instance variable - default
        self.name = "instance!"
    
    def __init__(self, name):
        # instance variable - specified
        self.name = name

    @classmethod # zClass = "Recipe"  
    def Create(zClass, zName):
        result = zClass() # Factory Op!
        result.name = zName
        return result

    @staticmethod
    def CreateNamed(name):
        result = NonInst()
        result.name = name
        return result

# Default initializer
dual = NonInst()
print(NonInst.name, dual.name)
print(type(dual))

# Paramaterized initializer(s)
dual = NonInst("MyVal")
print(NonInst.name, dual.name)
print(type(dual))

# Class method (factory -w- PARAM)
dual = NonInst.Create("Nagy")
print(NonInst.name, dual.name)

# Static method (factory -w- PARAM)
dual = NonInst.CreateNamed("Nagy")
print(NonInst.name, dual.name)

