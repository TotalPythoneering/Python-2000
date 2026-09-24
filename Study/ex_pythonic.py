# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_pythonic.py
# AUTHOR: Randall Nagy
#

def myfunc(ref):
    pass

zlist = [1, 2, 3]

# Not very Pythonic:
i = 0
zlist_length = len(zlist)
while i < zlist_length:
   myfunc(zlist[i])
   i += 1

# Extremely Pythonic:
for item in zlist:
   myfunc(item)  

# Not very Pythonic:
def eggs(a, b):
    a[0] = 3
    b[0] = 5.5

alpha = [0]
beta = [0]
eggs(alpha, beta)
alpha = alpha[0]
beta = beta[0]

# Extremely Pythonic:
def eggs():
    return 3, 5.5

alpha, beta = eggs()

import this

print(type(alpha))

      
