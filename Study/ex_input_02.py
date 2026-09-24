# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_input_02.py
# AUTHOR: Randall Nagy
#

name = input("Como te llamas? ")
print("Hello '", name, "'")
while True:
    try:
        age = input("What is your age? ")
        zage = int(age)
        print("%s is %d years old!" % (name, zage))
        break
    except ValueError:
        print("Sorry, that age is not numeric!")
    finally:
        print("Data entry completed!")





