#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyWhile02.py
# AUTHOR: Randall Nagy
#

class MyData(object):

    def readData(self):
        self.name = input("Como te llamas? ")
        
        while True:
            try:
                self.age = int(input("What is your age? "))
                break
            except ValueError:
                print("Sorry, that age is not numeric!")      

            
info = MyData()
info.readData()
print(info.name, "is", info.age)








