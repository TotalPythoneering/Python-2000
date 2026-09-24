# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyNumbers.py
# AUTHOR: Randall Nagy
# File: MyNumbers.py
#

ss = 0
while ss != 999:
    print(bin(ss))
    print(hex(ss))
    ss = input("Enter number: ")
    try:
        ss = int(ss)
    except Exception:
        ss = bytearray(ss, "ascii")
        ss = int.from_bytes(ss, byteorder='big')

        
    
    
