'''
This Is The Strings Section.
'''

# The objects holding the Strings are from the [Variable] section.
# If you do NOT understand what a variable is please head over to basics/Variables.py then return.
# A String is just a succession of characters.

STRING_CASE_ONE = ''
STRING_CASE_TWO = ""

# You may use either at any point in time.

# Examples:

my_string_one = 'this is a string'
my_string_two = "this also is a string"

# Something you will notice that will NOT work: 'This String Is Skrypt's'.
# Correction below:

example_0 = 'This String Is Skrypt\'s'

# Notice the [\] which escapes our first ['] and tells Python it is now a part of the expression not statement,
# this just means that it tells python that the ['] is taken at the literal character ['] and not a delimiter for Python to know when 
# the String ends.
# This also works:

example_0a = "This String Is Skrypt's" # Notice no [\] needed

# Using ["] we would need [\] while doing something like this:

example_0b = "Vivian Reads \"Strings\" As The Title Of This Script"

# Or alternatively:

example_0ba = 'Vivian Reads "Strings" As The Title Of This Script'

# The above output would be "Vivian Reads "Strings" As The Title Of This Script"

# There are a few neat things Python is able to do with Strings.
# Below are examples that use items from the [Functions, KeyWords, Operators] sections.
# If you get confused jump right over there and take a look and come back.

# One of the most common ways to use a String is to print() a message to the console.

print('this is what appears on your console')

# First useful function for Strings is len(), used to get the length of a String object (Other objects too).

example_1 = len(my_string_one) # Output: 16 (Notice Python also does not count the ['] String brackets)

# Strings support indexing, which just means that you can 'ask' for the character at a certain position.

example_1a = my_string_one[0] # Output: 't'

# You may also ask Python for a portion of a String using [:], this is called 'slicing'.
# Example [INT:]
# The below example will return the String atarting at the position 1: 'his is a string'.

example_1b = my_string_one[1:]

# The below example will return the portion starting at the postion 2 and ending at the position 4.
# Notice how we collect the character at position 2 but stop at position 3, position 4 is left out.

example_1c = my_string_one[2:4] # Output: 'is'

# To reverse a String the Pythonic term is either [::-1] on the end of any String expression, or the function
# reversed().

example_2 = 'normal string'
example_2a = example_2[::-1] # Output: 'gnirts lamron'
example_2b = example_2[2:5:-1] # Output: 'amr'

# Strings can be added together with the '+' operator.

example_3 = ''
example_3a = 'Hello'
example_3b = ' ' # Space
example_3c = 'World'
example_3d = example_3a+example_3b+example_3c # Output: 'Hello World'

# Alternatively:

example_3e = 'Hello'+' '+example_3c # Output: 'Hello World'
example_3 += example_3a[0] # Output: example_3 = 'H'

# Python has builtin methods for Strings like .upper(), .lower(), .title().

example_4 = 'our string'
example_4.upper() # Output: 'OUR STRING'
example_4.lower() # Output: 'our string'
example_4.title() # Output: 'Our String'
