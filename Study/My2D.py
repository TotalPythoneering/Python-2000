# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: My2D.py
# AUTHOR: Randall Nagy
# File: My2D.py
#

def draw(board):
    for row in board:
        print(row)
    print()

zD = [["1", "1", "1"],
      ["1", "1", "1"],
      ["1", "1", "1"],
      
      ["1", "1", "1"],
      ["1", "1", "1"],
      ["1", "1", "1"]]

for col in range(3):
    for row in range(2):
        try:
            zD[row][col] = 0
        except:
            print(row, col)
        draw(zD)
draw(zD)
