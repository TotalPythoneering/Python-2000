# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_exception_multi.py
# AUTHOR: Randall Nagy
#

import sys

try:
	file = open('myfile.txt')
	line = file.readline()
	ival = int(line.strip())

except IOError as ex:
        # How to test a "file not found" error?
	print("IOError({0}): {1}".format(ex.errno, ex.strerror))
	
except ValueError:
        # How to test the integer conversion error?
	print("Unable to convert line to integer.")
	
except:
        # How to test the catch-all error?
	print("Unexpected exception:", sys.exc_info()[0])

	
	








