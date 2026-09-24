# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 21:33:18
# FILE: MySorted.py
# AUTHOR: Randall Nagy
# File: MySorted.py
#

def show(zData):
    print(type(zData), "-", zData)
  
# Any iterable will do
show(sorted(("Mr. Ed", "Miss Daisy",
              "Mr. T", "Dr. Who"))) # Tuple
show(sorted(["Mr. Ed", "Miss Daisy",
              "Mr. T", "Dr. Who"])) # List
show(sorted({"Mr. Ed", "Miss Daisy",
              "Mr. T", "Dr. Who"})) # Set
show(sorted({4:"Mr. Ed", 2:"Miss Daisy",
              3:"Mr. T", 1:"Dr. Who"})) # Dict (keys)

# Original unchanged
foo = {4:"Mr. Ed", 2:"Miss Daisy",
              3:"Mr. T", 1:"Dr. Who"}
print(type(foo.values()))
print(type(foo.keys()))
print(foo.values())
show(sorted(foo))
print(foo.values())
