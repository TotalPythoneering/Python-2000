# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_OrderedDict.py
# AUTHOR: Randall Nagy
# Allows Access
# =============
#

# Package Qualification Required
import collections
bog = collections.OrderedDict(foo="bar", foo2="net")

print(type(bog))


# Add to "Local Namespace"

from collections import OrderedDict
bog = OrderedDict(foo="bar", foo2="net")

print(type(bog))




