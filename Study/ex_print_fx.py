# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_print_fx.py
# AUTHOR: Randall Nagy
#
print("First: %5d, Second: %05d" % (42,24)) # single prefix
print("First: {%05d}, Second: {%5d}" % (42,24)) # { } ignored
print("Name [%-20s], Age: %03d, Balance: $%7.2f" % ("Godzilla", 64, 22.42))
print("Name [%20s], Age: %03d, Balance: $%07.2f" % ("Godzilla", 64, 22.42))
# Error: Used more than once
print("More: %6.2f or %6.3f" % (5.1234))

