# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_builtins.py
# AUTHOR: Randall Nagy
# File: ex_builtins.py
# Show the __builtins__
# =====
#

ins = dir(__builtins__)

for count, avail in enumerate(ins,1):
    if count % 3 == 0:
        print(avail.center(25))
        continue
    print(avail.center(25) , end='')


import builtins
help(builtins)


