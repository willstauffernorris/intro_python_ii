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

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player = Player(name="Will", current_room="outside")
room_object = Room(player.current_room, room[player.current_room])


## Intro line
print("\n ~~~~~⛰ Welcome adventurer! ⛰~~~~~~\n ~~~~~~~* Begin the game. *~~~~~~~~~\n")

## Get player name

player_name_input = input("Enter your name, seeker 👉: ")
player.name = player_name_input
print("\n")


# Write a loop that:
while True:
    #Prints the current room name
    current_room_name = player.current_room
    ## The stuff in front of 'player name' makes the name bold
    print('\033[1m' +f"{player.name} " + '\033[0m' + f"arrives in the {current_room_name}.")

    # Prints the current description (the textwrap module might be useful here).
    current_room_description = room[current_room_name]
    print(f"""{current_room_description}""")
    print("~~~~~~~~~~~\n")

    # The input command parser
    # It waits for user input and commands to move to rooms in the four cardinal directions.
    # Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
    user_input = input("Please enter a cardinal direction, eg 'n' 👉: ")

    if user_input is 'n':
        print(f"""\n~~~~~~~~~~\n ⬆️  You are moving north, away from the {player.current_room}.""")
        player.current_room = room_object.n_to()

    elif user_input is 's':
        print(f"""\n~~~~~~~~~~\n ⬇️  You are moving south, away from the {player.current_room}.""")
        player.current_room = room_object.s_to()
        
    elif user_input is 'e':
        print(f"""\n~~~~~~~~~~\n ➡️ You are moving east, away from the {player.current_room}.""")
        player.current_room = room_object.e_to()

    elif user_input is 'w':
        print(f"""\n~~~~~~~~~~\n ⬅️  You are moving west, away from the {player.current_room}.""")
        player.current_room = room_object.w_to()

    # If the user enters "q", quit the game.
    elif user_input is 'q':
        print("You are quitting the game")
        break
    # Print an error message if the movement isn't allowed.
    #  The parser should print an error if the player tries to move where there is no room.
    ## This needs improved
    else:
        print("Please input a valid direction (n,s,e,w)")