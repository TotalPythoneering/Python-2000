# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-03-01 17:04:02
# FILE: MyWrapTest.py
# AUTHOR: Randall Nagy
# from "MyWrap.py" import "MyWrap"
#
from MyWrap import MyWrap
# from "MyWrap.py" import "Vola"
from MyWrap import Vola

file = "./MyWrap.txt"

ofile = Vola(file, "w")
with ofile:
	print(str(type(ofile)))
	ofile.writeLines(["zAble", "zBaker", "zZulu"])

ifile = Vola(file, "r")
with ifile:
    data = ifile.readLines()
    for ref in data:
        print(ref, end = "")


