#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2019-01-05 07:13:44
# FILE: MyOptionBase.py
# AUTHOR: Randall Nagy
#

zwork = dict()

zwork[16] = hex(321)
zwork[8] = oct(321)
zwork[0] = bin(321)

for key in zwork:
    print("Converted", zwork[key],
          "as", int(zwork[key], base=key))


