from room import Room
from player import Player

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
player = Player(name="Will", current_room="outside")
room_object = Room(player.current_room, room[player.current_room])

print(f'testing room name print: {room_object.name}')
# Write a loop that:

#Prints the current room name
current_room_name = player.current_room
print(f"{player.name}'s current room: {current_room_name}")

# Prints the current description (the textwrap module might be useful here).
current_room_description = room[current_room_name]
print(current_room_description)

print(room_object.n_to)

# Create the input command parser in `adv.py`
#Waits for user input and decides what to do.
#and commands to move to rooms in the four cardinal directions.
user_input = input("Please enter a cardinal direction, eg 'n'")
# If the user enters a cardinal direction, attempt to move to the room there.
# Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
# After each move, the REPL should print the name and description of the player's current room
#user_input = user_input.lower() ## This logic doesn't work yet
if user_input is 'n':
    print(f"You are currently in the {player.current_room}.")
    print("You are moving north.")

    player.current_room = room_object.n_to
    print(f'You are now in the {player.current_room}.')
elif user_input is 's':
    print("You are moving south")
elif user_input is 'e':
    print("You are moving east")
elif user_input is 'w':
    print("You are moving west")
# If the user enters "q", quit the game.
elif user_input is 'q':
    print("Quit the game")
# Print an error message if the movement isn't allowed.
#  The parser should print an error if the player tries to move where there is no room.
## This needs improved
else:
    print("Please input a valid direction (n,s,e,w)")