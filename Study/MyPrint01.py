#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyPrint01.py
# AUTHOR: Randall Nagy
#

data = {"First":"John",
        "Last":"Doe",
        "Phone":"123-456-7890",
        "Email":"foo@bar.net"}

zkeys = data.keys()

# Member lookup
for zkey in zkeys:
        print("%10s:[%-20s]" % (zkey, data.get(zkey)))
print()
# Natural lookup
for zkey in zkeys:
        print("%10s:[%-20s]" % (zkey, data[zkey]))


