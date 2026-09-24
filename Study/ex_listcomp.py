# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-25 15:30:00
# FILE: ex_listcomp.py
# AUTHOR: Randall Nagy
#


print("One")

for ch in "Soft9000":
    ich = ord(ch)
    print("%04X-" % ich, end = '')

print("\nTwo")

print([(hex(ord(ch))) for ch in "Soft9000"])

print("Three")

print([(x, y) for x in "abc" for y in "abc" if x is not y])

print("Four")

result = []
for x in "abc":
    for y in "abc":
        if x is not y:
            result.append((x, y))
 
print(result)


