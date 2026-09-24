# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_and_or_not.py
# AUTHOR: Randall Nagy
#
print ("Enter 1 or 0: ")
isFun = int(input("isFun? "))
isTough = int(input("isTough? "))

if isFun and isTough:
    print("We get what we pay for?")

if isTough or isFun:
    print("One 'outta 2 ain't bad!")

if not isFun:
    print("Practice makes it fun!")
    
if not (isTough and isFun):
    print("Learn C/C++?")


