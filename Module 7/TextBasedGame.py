# Jeremy Ayala
# Night at the Magic Kingdom text based game

import time #imported to attempt to slow down text output to the terminal but doesnt look like it worked

# defining main menu function. Googled and found that I could pass in ASCII art from a text file.

def main_menu():
    # Was trying to figure out how to get ascii art to print... found that I can put it in a text file
    with open("MK.txt") as f:
        print(f.read(), end='') #reading text file
        time.sleep(4)

#function to move between lands with argunment for current land, movement and land dict

def move_between_lands(current_land, move, lands):
    # move to corresponding land
    return lands[current_land].get(move, current_land)  # returh same land if invalid argument


def get_item(current_land, lands, inventory):
    # get item from current land and add to inventory if not already in.
    if 'item' in lands[current_land]:
        inventory.append(lands[current_land]['item'])
        print(f'You have picked up the {lands[current_land]["item"]}!')
        del lands[current_land]['item']
    else:
        print("There's nothing to pick up here.")

def display_welcome_message(current_land, inventory):
    print(f'\nWelcome to {current_land}!')
    print(f'Here is what you have in your bag: {inventory}')


# defining main function

def main():
    # dictionary of connecting MK lands with items within
    lands = {
        'Main Street U.S.A.': {'North': 'The Hub', 'South': 'TTC'},
        'The Hub': {'North': 'Fantasyland', 'East': 'Tommorowland', 'South' : 'Main Street U.S.A.','West':'Liberty Square'},
        'Tommorowland': {'West': 'The Hub', 'North':'New Fantasyland', 'item': 'Mickey Pretzel'},
        'Fantasyland': {'East': 'New Fantasyland', 'South': 'The Hub', 'West': 'Liberty Square', 'item': 'Cell Phone'},
        'New Fantasyland': {'West': 'Fantasyland', 'South':'Tomorrowland','item': 'Mouse Ears'},
        'Liberty Square': {'West': 'Adventureland', 'East':'The Hub','item': 'Turkey Leg'},
        'Adventureland': {'North': 'Frontierland','East':'Liberty Square', 'item': 'Dole Whip'},
        'Frontierland': {'South': 'Adventureland', 'item': 'Beignet'},
        'TTC': {}  # TTC is the final location
    }

    # list for inventory of player
    inventory = []

    # You start out in Main Street U.S.A.

    current_land = "Main Street U.S.A."

    # Call the main menu function
    main_menu()

    while True:
        # Logic to handle when you meet the Wizard at the TTC. Checks inventory length.
        if current_land == 'TTC':
            # winning logic
            if len(inventory) == 6:
                print('Congratulations! You have satisfied the Wizards demands and can go home now!')
                print('Thank you for playing!')
            else:
                # Game over logic
                print('\nHahahah! You did not get all of your missing items!')
                print('You were sentenced to eternity at the Magic Kingdom by the Wizard!')
                print('I hope you like Mickey Ice Cream Bars and Turkey Legs!')
                print('Thank you for playing!')
            break

        # Call to function to display current status
        display_welcome_message(current_land, inventory)

        # tell the user if there is an item in the land
        if 'item' in lands[current_land]:
            print(f'I think there might be {lands[current_land]["item"]} in this land!')
        print('------------------------------')

        # ask user for next move
        move = input('What land would you like to go to next? : ').title().split()

        # logic if the user enters a command to move to a new land
        if len(move) >= 2 and move[0].capitalize() == 'Move' and move[1] in lands[current_land]:
            current_land = move_between_lands(current_land, move[1], lands)

        # logic if the user enters a command to get an item
        elif len(move) >= 2 and move[0].capitalize() == 'Get':
            get_item(current_land, lands, inventory)

        # logic if the user enters an invalid entry
        else:
            print('You cannot move to this location or did not enter Move , please try again.')


if __name__ == "__main__":
    main()