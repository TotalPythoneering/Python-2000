#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_python_framework.py
# AUTHOR: Randall Nagy
#

class MyGreater(int):
  age = 0
  def __init__(self, age):
    self.age = age
  
  def __gt__(self, comp):
    print("Python Framework calls __gt__(...)!")
    return super.__gt__(self, comp)
           
comp1 = MyGreater(123)
comp2 = MyGreater(345)
print(comp1 > comp2)








