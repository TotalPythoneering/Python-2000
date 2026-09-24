# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_yeild.py
# AUTHOR: Randall Nagy
# # yield
#

def subset(arg):
    # Yield = Add "expression" to result
    for a in arg:
        if a % 2 == 0:
            yield a

items = [1, 2, 3, 4, 5, 6]

# Show yield items returned
copy = list(subset(items))
print("subset:",copy)

    
