# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ez_zip.py
# AUTHOR: Randall Nagy
#

lc01 = [(hex(ord(ch))) for ch in "Soft9000"]
lc02 = [(chr(int(ch, 16))) for ch in lc01]

print("lc01", lc01)
print("lc02", lc02)



combined = zip(lc01, lc02)
print("combined", combined)




print("*combined",*combined)

