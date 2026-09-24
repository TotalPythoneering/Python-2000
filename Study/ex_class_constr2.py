#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_class_constr2.py
# AUTHOR: Randall Nagy
#

class MyData(object):   
  def __init__(self):
    self.name = 'default'
    self.age = 999
  def InputData():
    result = MyData()
    result.name = input("Como te llamas? ")      
    while True:
      try:
        result.age = int(input("What is your age? "))
        break
      except ValueError:
        print("Sorry, that age is not numeric!")
      finally:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return result

      
info = MyData.InputData()
print(info.name, "is", info.age)













