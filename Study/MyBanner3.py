#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyBanner3.py
# AUTHOR: Randall Nagy
#
def ShowChars(num, token):
        return "\t{}".format(token * (num + 4))
                        
def Show(message):
        stars = ShowChars(len(message), '*')
        print(stars)
        print("\t**{0:%<s}**".format(message))
        print(stars)

Show(" SPECIAL ")
Show(" SALE ")

