# This is a program that will ask for the users name and age

# Take user's name as in input and store into user_name variable

user_name = input("What is your name?: ")

# take user's year of birth as inout

user_age = input("How old are you?:")

# Logic to subtract user age from current year to get yeaar of birth

user_yob = int(2024) - int(user_age)

# Returning the input

print('Hello', user_name, '! You were born in ', user_yob, '.')
