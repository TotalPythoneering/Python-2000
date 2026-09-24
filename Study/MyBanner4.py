#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyBanner4.py
# AUTHOR: Randall Nagy
#
def MkString(num, token):
        return "{}".format(token * num)
                        
def Show(message):
        stars = MkString(20, '*')
        print(stars.center(20))
        print(message.center(20))
        print(stars.center(20))
        
Show(" SPECIAL ")
Show(" SALE ")

