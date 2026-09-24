# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_Lambda.py
# AUTHOR: Randall Nagy
# single statement
#   - no block(s)
#   - no compounds (;)
# do not use return
#
lamba = lambda x: x * 2
print(lamba(12))

# multiple parameters okay
# may call other functions (etc.)
lambb = lambda x, y, z:  lamba(x) + (y * 2) + (z * 2)
print(lambb(12, 13, 14))



        
