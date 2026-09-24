# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-02-20 15:30:00
# FILE: ex_format_fx.py
# AUTHOR: Randall Nagy
#
print("First: {0}, Second: {1}".format(42,22))
print("First: {}, Second: {}".format(22.42,42))
print("Second: {1}, First: {0}".format(42,22))
print("Second: {1:3d}, First: {0:7.2f}".format(22.42,42))

print("First: {foo}, Second: {bar}".format(foo=22.42,bar=42))
print("Second: {bar}, First: {foo}".format(foo=22.42,bar=42))


print("Name [{0:12s}], Age: {1:03d}, \
Blanace: ${2:07.2f}".format("Client", 64, 22.42))

print("Name [{0:>12s}], Age: {1:<d}, \
Balance: ${2:<7.2f}".format("Client", 64, 22.42))

# Used more than once:
print("More: {0:6.2f} or {0:6.3f}".format(5.1234))


# Extra parameters ignored:
print("More: {1:6.2f} or {1:6.3f}".format(12.345, 5.1234))

print("The \
is a \
                  TEST!")


