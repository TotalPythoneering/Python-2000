# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-03-01 15:30:00
# FILE: ex_with_file_io.py
# AUTHOR: Randall Nagy
#


file = "./withio.txt"

with open(file, "w") as ofile:
    print("write: " + str(type(ofile)))
    data = "One Two Three".split(" ")
    for ss, ref in enumerate(data, 1000):
        ofile.write("Saving " + str(ss) + " as " + str(ref))
        ofile.write("\n")
    # implicit close

with open(file, "r") as ifile:
    print("read: " + repr(type(ifile)))
    data = ifile.readlines()
    for ref in data:
        print(ref, end = "")
    # closed, too


