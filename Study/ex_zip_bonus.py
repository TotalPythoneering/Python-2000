# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-12-08 15:30:00
# FILE: ex_zip_bonus.py
# AUTHOR: Randall Nagy
# ex_zip_bonus
#

labels = ("Name", "Age")

data = [
    ("Sue", 27),
    ("John", 37),
    ("Bungee", 47),
    ]

for row in data:
    print(*zip(labels, row))


