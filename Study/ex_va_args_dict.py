#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ex_va_args_dict.py
# AUTHOR: Randall Nagy
#

def args(**argv):
    print(type(argv))
    for count, ref in enumerate(argv.values()):
        print(count, ref)

args()
args(op="dCombine:", fi="dOne", se="dTwo", th="dThree")
# args("Combine:", "One", "Two", "Three") # Error -  Not a Dictionary
# args("Combine:", 1, 2.2, 3.73e121)      # Error -  Not a Dictionary


