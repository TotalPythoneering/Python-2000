# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_imports_as.py
# AUTHOR: Randall Nagy
# Module "ex_import_as.py"
#
""" Simple Module & Importation """

from NewThing.MyNewThing import CallaFunc as Calla

print("__doc__:", Calla.__doc__, end="\n\n-~=*=~-\n\n")

help(Calla)

print("aka: Calla():", Calla())

from NewThing import DoTheThing
#print('before', DoTheThing)



