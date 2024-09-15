# This is a program that will ask for the users name and age

# Take user's name as in input and store into user_name variable

userName = input("What is your name?: ")

# take user's year of birth as inout

userAge = input("How old are you?:")

# Logic to subtract user age from current year to get yeaar of birth

userYob = int(2024) - int(userAge)

# Returning the input

print('Hello', userName, '! You were born in ', userYob, '.')