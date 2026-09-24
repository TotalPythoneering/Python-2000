# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-03-01 15:30:00
# FILE: ex_super_init.py
# AUTHOR: Randall Nagy
#


class MyBase:
    def __init__(self):
        self.value = "base"


class MyChild(MyBase):
    def __init__(self):
        self.unique = 1
        self.value = "child"
        super().__init__()


var = MyChild()

print(var.value, var.unique)

class MyGrandChild(MyChild):
    def __init__(self):
        self.unique = 9
        self.value = "Grand"
        super(MyBase, self).__init__()

var = MyGrandChild()

print(var.value, var.unique)

