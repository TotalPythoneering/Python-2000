# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ex_zip_dict.py
# AUTHOR: Randall Nagy
#

d01 = {'a':1, "b":2 }

d02 = {"c":1, 'd':2 }


print(*zip(d01, d02))

print(*zip(*d01, *d02))

print("s1",*zip(sorted(d01), sorted(d02)))
print("s2",sorted(*zip(*d01, *d02)))


