# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-11-28 03:44:26
# FILE: MydSort.py
# AUTHOR: Randall Nagy
# File: MydSort.py
#

#import os
#print(os.environ['PYTHONHASHSEED'])
#print(os.environ)

def sort_by_hash2(zData):
    import hashlib
    return hashlib.md5(bytes(zData,"utf8")).hexdigest()
def sort_by_hash(zData):
    import zlib
    return zlib.crc32(bytes(zData,"utf8"))
def sort_by_len(zData):
    return len(zData)
def sort_by_last(zData):
    zUpper = zData.upper() # Upper Case
    return zUpper[len(zData) - 1] # Last Char

foo = {4:"Mr. Ed", 2:"Miss Daisy",
       3:"Mr. T",  1:"Dr. Who"}
zValues = list(foo.values())
print("normalized:\t", zValues)
zValues.sort(key=sort_by_hash)
print("by hashcode:\t",zValues)
zValues.sort(key=sort_by_len)
print("by length:\t", zValues)
zValues.sort(key=sort_by_last)
print("by last char:\t", zValues)



