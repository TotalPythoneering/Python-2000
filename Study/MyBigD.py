# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyBigD.py
# AUTHOR: Randall Nagy
# File: MyBigD.py
#

def draw(board):
    for row in board:
        print(row)
    print()

print("Asymmetrical")
asym = [[1], [1, 1],
        [1, 1, 1],
        [1, 1, 1, 1]]
for row in range(len(asym)):
        try:
            zRow = asym[row]
            for col in range(len(zRow)):
                zRow[col] = 0
        except:
            print(row, col)
        draw(asym)


