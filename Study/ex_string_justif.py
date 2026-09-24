# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_string_justif.py
# AUTHOR: Randall Nagy
#


str = "Booya"
print("[",str.center(12), "]")

print("[",str.ljust(12), "]")

print("[",str.rjust(12), "]", sep='')

# Handy!
print("fill: [",str.rjust(12, "*"), "]", sep='')
print("fill: [",str.ljust(12, "*"), "]", sep='')
print("zfill: [",str.zfill(12), "]", sep='')

