#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ex_va_args.py
# AUTHOR: Randall Nagy
#

def args(*argv):
    print(type(argv))
    for count, ref in enumerate(argv):
        print(count, ref)

args()
args("Combine:", "One", "Two", "Three")
args("Combine:", 1, 2.2, 3.73e121)
# args(op="dCombine:", fi="dOne", se="dTwo", th="dThree") # Error - IsA Dictionary!


