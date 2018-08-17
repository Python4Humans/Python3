"""
A Place For All Variable Data
"""

 # A Variable Is The Main Data Container That Most Programming Languages Use.
 # Most Common Question I Always Get When People See:
 x = 0
 y = 1
 xy = x+y
 yx = y+x
 # Is How Do You Know That x = 0....
 # The Magic Is We Don't It Could Have Been:
 Work = 0
 Sucks = 1
 WorkSucks = Work+Sucks
 SucksWork = Sucks+Work
 # Presto! We Name Our Own Variables What Ever We Choose.
 # No One Will Ever Be Able To Care Unless They See The Code Base
 # Variable Names Do Not Show In Production / Execution. Only Their Values.

 # Variables Can Contain Anything Some But Not All Examples:

 string = 'I\'m A Real String!'
 number = 0
 boolean = True
 none = None

 # Variables Should Never Be The Same As Keywords As In list,hex,dict,if,elif,else,for
 # It's Good Practice To Uppercase All Variables That Will Stay The Same Throughout Execution
 # Example:
 PROGRAM_NAME = 'Variables.py'
 # In The Functions Area [os,sys] Both Have Unique Ways Of Grabbing This Files Name 
 # This Becomes Useful Incase It Is Changed By You || A User.