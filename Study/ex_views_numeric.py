#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_views_numeric.py
# AUTHOR: Randall Nagy
#

def numView(v):
  print("-----")
  dat = (v, hex(v), oct(v), bin(v))
  for d in dat:
    print(type(d), d)

numView(1)
numView(21)
numView(31)
numView(42)












