# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_exception_custom.py
# AUTHOR: Randall Nagy
#

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

try:
    # Using
    raise MyError("Tossing it in!")
except Exception as ex:
    print("Catch-all:", ex)
else: # New!
    print("All is well!")

try:
    pass
except Exception as ex:
    print("Catch-all:", ex)
else:
    print("All is well!")    
    
try:
    # Select ONE of the following
    raise MyError("Tossing it in!")
    # ss = 12 / 0
    # pass
except Exception as ex:
    # Select EITHER of the following
    print("Got:", ex)
    # raise
else:
    print("All is well!")








