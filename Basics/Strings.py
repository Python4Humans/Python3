'''
 This Is The Strings Section.
 '''

# The Objects Holding The Strings Are From The [Variable] Section
# If You Do NOT Understand What A Variable Is Please Head Over To Basics/Variables.py Then Return.
# A String Is Anything Interpreted To Be Read.
STRING_CASE_ONE = ''
STRING_CASE_TWO = ""
# You May Use Either At Any Point In Time.

# Examples:
my_string_one = 'this is a string'
my_string_two = "this also is a string"

# Something You Will Notice That Will NOT Work: 'This String Is Skrypt's'
# Correction Below:
example_0 = 'This String Is Skrypt\'s'
# Notice The [\] Which Escapes our First ['] And Tells Python It Is Now Apart Of The Expression Not Statement.
# This Also Works
example_0a = "This String Is Skrypt's" # Notice No [\] Needed
# Using ["] We Would Need [\] While Doing Something Like This
example_0b = "Vivian Reads \"Strings\" As The Title Of This Script"
# Or Alternativly
example_0ba = 'Vivian Reads "Strings" As The Title Of This Script'
# Above Output Would Be "Vivian Reads "Strings" As The Title Of This Script"

# There Are A Few Neat Things Python Is Able To Do With Strings.
# Below Are Examples That Use Items From The [Functions,KeyWords, Operators] Sections
# If You Get Confused Jump Right Over There And Take A Look And Come Back.

# First Usefule Item For Strings Is len() Used To Get The Length Of A String Object (Other Objects Too)
# Normally Python Would Start At 0 With Counting But This Isn't The Case Here
example_1 = len(my_string_one) 
# Output Is [16] Notice Python Also Does Not Count The ['] String Brackets
# Strings Have Positional Memory That Python Can Choose With A Integer.
example_1a = my_string_one[0]
