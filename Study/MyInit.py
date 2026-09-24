#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyInit.py
# AUTHOR: Randall Nagy
#

class MyInit(object):
  def _update(self, name, age): # Private
    self.name = name
    self.age = age
    
  def __init__(self, name, age): # Constructor
    self._update(name, age)
    
  def update(self, name, age): # Public
    self._update(name, age)
           
info = MyInit("Nagy", 123)
print(info.name, "is", info.age)
info.update("Tom", 23)
print(info.name, "is", info.age)



