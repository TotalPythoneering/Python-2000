# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_enumerate_sys_modules.py
# AUTHOR: Randall Nagy
#
import sys

for zIndex, zNode in enumerate(sys.modules):
    print(zIndex + 1, zNode)

