# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_global.py
# AUTHOR: Randall Nagy
# Demonstrate MODULARIZED "GLOBAL"
# =====
#

DoTheThing = "Default 'thang."

def ZapTheThing(): # Define
    """ Demonstrate Global """
    global DoTheThing
    DoTheThing = "New Thing!" # Global!

DoTheThing = "GLOBAL"
print('Default:', DoTheThing)
ZapTheThing()
print('Updated:', DoTheThing)

def ZapTheThing():  # Re-defined
    """ Demonstrate Local """
    DoTheThing = "LOCAL ONLY" # Local!

DoTheThing = "GLOBAL"
print('Default:', DoTheThing)
ZapTheThing()
print('NOT UPDATED:', DoTheThing)



