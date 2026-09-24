# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyArrayAsymetric.py
# AUTHOR: Randall Nagy
# File: MyAsymetric.py
#

def draw(board):
    for row in board:
        print(row)
    print()

print("Asymetrical")
sym = [
    ["a", "b", "c"],
    ["a", "b",
    ["a", "b", "c"] ]

# We can always fall back to:
for row in range(len(sym)):
        try:
            zRow = sym[row]
            for col in range(len(zRow)):
                zRow[col] = 0
        except:
            print(row, col)
        draw(sym)
