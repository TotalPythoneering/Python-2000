# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MyThingUser.py
# AUTHOR: Randall Nagy
# MyThingUser.py
#

import NewThing
print("_init__ doc:\n=====\n")
help(NewThing)
dir(NewThing)

print("Import Module:\n=====\n")
import NewThing.MyNewThing
help(NewThing.MyNewThing)
dir(NewThing.MyNewThing)

print("Module as Alias:\n=====\n")
import NewThing.MyNewThing as booya
help(booya)
dir(booya)

