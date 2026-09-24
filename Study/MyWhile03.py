#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyWhile03.py
# AUTHOR: Randall Nagy
#

class MyData(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def InputData():
    result = MyData("Que?", -1)
    result.readData()
    return result
  def readData(self):
    self.name = input("Como te llamas? ")      
    while True:
        try:
            self.age = int(input("What is your age? "))
            break
        except ValueError:
            print("Sorry, that age is not numeric!")
        finally:
            print("...")
           
info = MyData("Nagy", 123)
print(info.name, "is", info.age)
info = MyData.InputData()
print(info.name, "is", info.age)








