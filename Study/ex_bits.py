#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_bits.py
# AUTHOR: Randall Nagy
#

num = 321
print("Numeric Views")
print("As Decimal:", num)
print("As Hex:", hex(num))
print("As Octal:", oct(num))
print("As Binary:", bin(num))
print("~~~~~")

value = 0xA # Newline
print("String Views")
print("Dec:", value)
print("Hex:", hex(value))
print("Oct:", oct(value))
print("Bin:", bin(value))
print("~~~~~")

for val in range(0x20, 0x80):
    print("%s(%s)" % (hex(val),chr(val)), end="")
    if (val % 8 == 0):
        print()

        
