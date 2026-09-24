# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2018-05-24 15:30:00
# FILE: ex_multi_inherit01.py
# AUTHOR: Randall Nagy
# ex_multi_inherit01
#

class BaseA():
    def walk(self):
        print("walking...")
        
class BaseB():
    def talk(self):
        print("talking...")

class C(BaseA, BaseB):
    pass


c = C()
c.walk()
c.talk()



