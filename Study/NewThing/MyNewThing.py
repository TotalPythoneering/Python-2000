# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2017-02-20 15:30:00
# FILE: MyNewThing.py
# AUTHOR: tbd.
# Module "MyNewThing.py"
#
""" MyNewTging:
    An arbitrary module in a package.
"""

class ClassDoc:
    def foo():
        """ Take a pass at foo """
        pass
    def eggs():
        """ Take a pass at eggs """
        pass
    
def CallaFunc():
    """ CallaFunc: Demonstrate Simple Importation """
    return "Greetings from CallaFunc!"

def ZapTheThing():
    """ ZapTheThing: Demonstrate NO GLOBAL! """
    global DoTheThing
    DoTheThing = "Zapped!" # Still Local
    return "Greetings from ZapTheThing!"

