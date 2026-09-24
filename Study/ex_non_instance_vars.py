# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_non_instance_vars.py
# AUTHOR: Randall Nagy
# File: ex_non_instance_vars.py
#

class NonInst:
    # class variable - common to all!
    name = "class_var"
    
    def __init__(self):
        # instance variable
        self.name = "instance!"

# Same .name - two values!
dual = NonInst()
print("Class .name:", NonInst.name)
print("Instance .name:", dual.name)

