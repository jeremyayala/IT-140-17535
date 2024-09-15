# This is a program that will ask for the users name and age and output their date of birth
# Take user's name as in input and store into userName variable

userName = input("What is your name?: ")

# take user's year of birth as input and store into userAge variable

userAge = input("How old are you?:")

# Logic to subtract userAge from current year to get year of birth

userYob = int(2024) - int(userAge)

# Printing the output to the command line

print('Hello', userName, '! You were born in ', userYob, '.')