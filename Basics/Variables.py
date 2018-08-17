"""
A place for all variable data
"""

# A variable is the main data container that all programming languages use.
# Most common question I always get when people see:
x = 0
y = 1
xy = x+y
yx = y+x
# Is how do you know that x = 0....
# The magic is we don't it could have been:
Work = 0
Sucks = 1
WorkSucks = Work+Sucks
SucksWork = Sucks+Work
# Presto! We name our own variables what ever we choose.
# No one will ever be able to care unless they see the code base
# Variable names do not show in production / execution. Only their values.

# Variables can contain anything some but not all examples:

string = 'I\'m A Real String!'
number = 0
boolean = True
none = None

# Variables should never be the same as keywords as in list,hex,dict,if,elif,else,for
# It's dood practice to uppercase all variables that will stay the same throughout execution
# Example:
PROGRAM_NAME = 'Variables.py'
# In the functions area [os,sys] both have unique ways of grabbing this files name 
# This becomes useful incase it is changed by you || a user.