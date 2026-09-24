# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_sorted_types.py
# AUTHOR: Randall Nagy
# File: ex_sorted_types.py
# Any iterable will do
#
zset = {"Mr. Ed", "Miss Daisy", "Mr. T", "Dr. Who"}

print(sorted(zset)) # Tuple

print(sorted(zset, reverse=True)) # Tuple


def sortLogic(ref):
        return len(ref)

print(sorted(zset, key=sortLogic, reverse=True)) # Tuple


