# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-03-01 15:30:00
# FILE: ex_super_func.py
# AUTHOR: Randall Nagy
#

class MyBase:
    def __init__(self):
        pass

    def GetCode(self):
        return "BaseCode"


class MyChild(MyBase):
    def __init__(self):
        pass

    def GetCode(self):
        return "Re-Use " + super().GetCode()


var = MyChild()
print(var.GetCode()) # "Re-Use BaseCode"


class MyGrandChild(MyChild):
    def __init__(self):
        pass
    
    def GetCode(self):
        try:
            # Error: Only works for directed-construction:
            return super(MyBase, self).GetCode()
        except Exception as ex:
            print("Whoops!", str(ex) + "???")
            return super().GetCode()
    
var = MyGrandChild()

print(var.GetCode())

