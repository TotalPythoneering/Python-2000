# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2018-05-24 15:30:00
# FILE: ex_multi_inherit_02_diamond.py
# AUTHOR: Randall Nagy
# ex_multi_inherit_02_diamond.py
#

class BaseA():
    def walk(self):
        print("a walking...")
        
class BaseB():
    def walk(self):
        print("b walking...")

class C(BaseA, BaseB):
    pass

class D(BaseB, BaseA):
    pass


c = C()
c.walk()

d = D()
d.walk()



