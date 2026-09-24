#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_while_break_continue.py
# AUTHOR: Randall Nagy
#

num = 0x80
val = 0x20
while val <= 256:
    print("%s(%s)" % (hex(val),chr(val)), end="")
    val += 1
    if val % 8 == 0:
        print()
        continue
    if val >= num:
        break
    

        
