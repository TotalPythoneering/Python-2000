#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_id_dict.py
# AUTHOR: Randall Nagy
#

data = {"First":"John",
        "Last":"Doe",
        "Phone":"123-456-7890"}

print(data)  # Unchanged
byVal = data["Phone"]
byRef = id(data["Phone"]) # Still a copy!
data["Phone"] = "321-654-0987"
print(data)  # Changed
print("Unchanged:", byVal) # Preserved

import _ctypes
print("Re-reference:",_ctypes.PyObj_FromPtr(byRef))
print(byRef, id(byVal))


