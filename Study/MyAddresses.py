# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: MyAddresses.py
# AUTHOR: Randall Nagy
# File: MyAddresses.py
#

def dumper(theme, zlist):
    print(theme)
    for ref in zlist:
        print("\tAddress:", hex(id(ref)), "\t{}".format(ref))    
    print("Collection:", hex(id(zlist)))

# Original, Deep, and Shallow
zData = ["One", "Two", "Three"]
dumper("Original", zData)

cpDeep = list(zData)
dumper("Deep-copy", cpDeep)

cpShallow = zData
dumper("Shallow-copy", cpShallow)

# Change the Original
print("\n\nDRAMA & TRAMA\n")
zData[0] = "Big"
zData[1] = "Bad"
zData[2] = "Bit"

# Deep has Original
dumper("Original", zData)
dumper("Deep-copy", cpDeep)
dumper("Shallow-copy", cpShallow)


