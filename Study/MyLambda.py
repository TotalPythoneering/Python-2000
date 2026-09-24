# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2019-01-05 04:39:46
# FILE: MyLambda.py
# AUTHOR: Randall Nagy
# /usr/bin/env python3
#

print((lambda ival: (ival % 2))(2))

bonus = (lambda ival: (ival % 2))
print(type(bonus))
print(type(bonus(97)))
print(bonus(97))

