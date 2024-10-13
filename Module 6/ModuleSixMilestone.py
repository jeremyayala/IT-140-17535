# Jeremy Ayala
# Dictionary for moving between rooms in dragon themed game

rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

starting_location = 'Great Hall'

current_location = 'Great Hall'

# valid movements

movements = ['North','South','West','East']

# Start of the program. Getting Player Name

player_name = input("Please Enter Your Name: ")
print ('Welcome to the Dragons Lair', player_name,'!') #Not sure if this is called Dragons Lair :D
print ('You are in the',starting_location,'!') #Displaying current location
print('You can move North, South, West, or East') #Displaying list of commands

# Per flowchart, if players room is exit then we exit, So I'm thinking we can use a while loop to
# check the location

while current_location != 'Exit' :
    print(player_name,'You are in the', current_location,'!')
    player_command = input("Where would you like to move? : " ).title()
    #Added title function to convert all input to first letter capital and rest lower case.
    # Had issues when testing and using south vs South
    player_list = player_command.split() # Taking input and split to list to get input
    if player_command == 'Exit':
        print('Game Over. Thanks for playing!')  #Exiting if player wants to
        current_location = 'Exit'
    elif player_command in movements:
        #loop to check input. If input is in key in dictionary for current location then move to the location
        if player_list[0] in rooms[current_location]:
            current_location = rooms[current_location][player_list[0]]
        else:
            print('Wrong direction! Try again!') # Wrong direction or word input
    else:
        print('Wrong direction! Try again!')





