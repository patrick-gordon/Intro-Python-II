from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#Choice Options
game_items = {

    'Golden Spatula': Item('Golden Spatula', 'This item is plated in gold and could be worth a lot of money'),

    'Wooden Spear': Item('Wooden Spear', 'This item is a good weapon for fishing && fighting'),

    'Axe': Item('Axe', 'This item is a good weapon and can be used to cut down trees.'),

    'Medalion': Item('Medalion', 'This item is rare and is worth a lot of money' ),

    'Compass': Item('Compass', 'This item is worth very little money')
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.




newPlayer = Player('Pat', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(f'You are crrently: {newPlayer.current_room.name}\nDescription: {newPlayer.current_room.description}!\nWhere would you like to go?')


user = (input("[n] North [s] South [e] East [w] West [q] Quit \n ").lower())


"""
1. set variable to t/f for while loop (turn variable to false with input to quit?)

Any restrictions on what the comparative can be in while loop? whast the easiest in this situation?
"""
while True: 
    
    # quits game
    if user =='q':
        break
    
    #User is playing game
    elif user == 'n':
        if newPlayer.current_room.n_to:
            newPlayer.current_room = newPlayer.current_room.n_to
        else:
            print('There is no room to the north')
    
    elif user == 's':
        if newPlayer.current_room.s_to:
            newPlayer.current_room = newPlayer.current_room.s_to
        else:
            print('There is no room to the South')
    

    elif user == 'e':
        if newPlayer.current_room.e_to:
            newPlayer.current_room = newPlayer.current_room.e_to
        else:
            print('There is no room to the East')

    
    elif user == 'e':
        if newPlayer.current_room.w_to:
            newPlayer.current_room = newPlayer.current_room.w_to
        else:
            print('There is no room to the West')

    else:
        break

    print(f'You are crrently: {newPlayer.current_room.name}\nDescription: {newPlayer.current_room.description}!\nWhere would you like to go?')

    user = (input("[n] North [s] South [e] East [w] West [q] Quit \n ").lower())

    

   
    







"""


"""