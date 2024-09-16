# This is a program that will ask for the users name and age and output their date of birth
# Take user's name as in input and store into userName variable

from datetime import date

userName = input("What is your name?\n")

# take user's year of birth as input and store into userAge variable

userAge = int(input("How old are you?\n"))

# Logic to subtract userAge from current year to get year of birth

userYob = date.today().year - userAge

# Printing the output to the command line

print('Hello' + ' ' + userName + '! You were born in ', userYob, '.\n')