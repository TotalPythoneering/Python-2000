# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: My3D.py
# AUTHOR: Randall Nagy
# File: My3D.py
#

def draw(board):
    for row in board:
        print(row)
    print()

d3 = [[[1,1,1], [1,1,1], [1,1,1]],
      [[1,1,1], [1,1,1], [1,1,1]],
      [[1,1,1], [1,1,1], [1,1,1]],
      [[1,1,1], [1,1,1], [1,1,1]],
      [[1,1,1], [1,1,1], [1,1,1]],
      [[1,1,1], [1,1,1], [1,1,1]]]

for z in range(3):
    for y in range(3):
        for x in range(6):
            try:
                d3[x][y][z] = 0
            except Exception as ex:
                print(ex, x, y, x)
draw(d3)

