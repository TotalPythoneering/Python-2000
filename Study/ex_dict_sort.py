#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_dict_sort.py
# AUTHOR: Randall Nagy
#

def sortLogic(ref):
        return len(ref)

data = {"First":"John",
        "Last":"Doe",
        "Phone":"123-456-7890",
        "Email":"foo@bar.net"}

zkeys = list(data.keys())
zkeys.sort(key=sortLogic)

# Natural lookup
for zkey in zkeys:
        print("%10s:[%-20s]" % (zkey, data[zkey]))


