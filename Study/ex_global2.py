# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_global2.py
# AUTHOR: Randall Nagy
#
def Bigsky():
    global ThisString
    ThisString = "Default"

def Remote():
    print(ThisString)

Bigsky()              # Define into Global
print(ThisString)     # Proof
ThisString = "Spam!"  # Update Global
Remote()              # Proof


