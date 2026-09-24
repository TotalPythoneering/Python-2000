# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2024-06-03 09:35:50
# FILE: ex_match_case.py
# AUTHOR: Randall Nagy
# File: ex_match_case.py
# Since Python 10:
#

s = input("Enter a number: ")
match s:
    case '1':
        print("zOne!")
    case '2' | '3':
        print("Two or three...")
    case _:
        print(f"{s} is not zOne...")

