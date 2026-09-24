# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_UnorderedDict.py
# AUTHOR: Randall Nagy
# https://hg.python.org/cpython/file/3.5/Lib/pydoc.py
#

"""
Dictionary Demo
"""

__doc__ = "foo"

__all__ = ['help']

__author__ = "Da NAG"

__date__ = "25 September 2015"

def phatd(args):
    """ Demonstrate 'eccentric' ordering for dict """
##    for ref in args:
##        print(ref)
##    print("=====")
    for ref in args:
        print(ref, ", ", args[ref], end='', sep='')
    print()

def phat(**args):
    """ Demonstrate same ordering for inline-dict """
##    for ref in args:
##        print(ref)
##    print("=====")
    for ref in args:
        print(ref, ", ", args[ref], end='', sep='')
    print()

""" bla, bla, bla """
help(phat)
phat(name="foo", name2="bar", name3="net")
phat(name1="foo", name2="bar", name3="net")
phat(name4="foo", name2="bar", name3="net")
help(phatd)
phatd( {"name":"foo", "name2":"bar", "name3":"net"}   )
phatd( {"name1":"foo", "name2":"bar", "name3":"net"}   )
phatd( {"name4":"foo", "name2":"bar", "name3":"net"}   )

#help(__module__)
#help(__main__)

