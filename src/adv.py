from room import Room
from item import Item
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


item = {
    'sword': Item("Sword of Destiny", "Used for spreading cream cheese."),

    'torch' : Item("Flaming Hot Torch", "Used for lighting the way."),

    'coin' : Item("Shiny Golden Coin", "Can trade for dried fish.")
}

# Make a new player object that is currently in the 'outside' room.
player = Player(name="Will", current_room="outside")
room_object = Room(player.current_room, room[player.current_room])

#print(f'You have these items: {player.display_items()}.')

torch = Item("torch", "Used for lighting the way.")
sword = Item("sword", "Used for spreading cream cheese.")
coin = Item("coin", "Can trade for dried fish.")


#player.add_items(torch)
#player.add_items(sword)

#print(f'NOW, you have these items: {player.display_items()}.')
#print(player.items[2])
#print(player.display_items())

print("----------")


#print(f"The {room['outside'].name} contains these items: {room['outside'].display_items()}")
room['outside'].add_items(torch)
room['outside'].add_items(sword)
room['foyer'].add_items(coin)
# print(f"NOW, the {room['outside'].name} contains these items: {room['outside'].display_items()}")

## Intro line
print("\n ~~~~~⛰ Welcome adventurer! ⛰~~~~~~\n ~~~~~~~* Begin the game. *~~~~~~~~~\n >>>Press 'q' at any time to quit<<<\n >>>Press 'i' to view inventory<<<\n")

'''
## Get player name


player_name_input = input("Enter your name, seeker 👉: ")
player.name = player_name_input
print("\n")
'''


northlist = ['outside', 'foyer', 'narrow']
southlist = ['treasure', 'overlook', 'foyer']
eastlist = ['foyer']
westlist = ['narrow']

valid_list = ['n','s', 'e', 'w', 'i']

print()
# Write a loop that:
while True:
    #Prints the current room name
    current_room_name = player.current_room
    ## The stuff in front of 'player name' makes the name bold
    print('\033[1m' +f"{player.name} " + '\033[0m' + f"arrives in the {room[current_room_name].name}.")

    # Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
    print(f"The {room[current_room_name].name} contains these items: {room[current_room_name].display_items()}")

    # Prints the current description (the textwrap module might be useful here).
    current_room_description = room[current_room_name]
    print(f"""{current_room_description}""")
    
    print("~~~~~~~~~~~\n")

    # The input command parser
    # It waits for user input and commands to move to rooms in the four cardinal directions.
    # Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
    user_input = input("Please enter a cardinal direction (n,s,e,w) \nOR a command (get,drop) an item 👉: ")
    print("~~~~~~~~~~~\n")

    # Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.
    split_input = user_input.split(" ")

    # Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser
    if len(split_input) == 2:
        # Implement support for the verb get followed by an Item name. This will be used to pick up Items.
        # such as "take coins" or "drop sword"


# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

# If it is there, remove it from the Room contents, and add it to the Player contents.

# If it's not there, print an error message telling the user so.


# Call on_take method in Item. when the Item is picked up by the player.
# Implement support for the verb drop followed by an Item name. This is the opposite of get/take.



        if split_input[0] == 'get':
            player.add_items(item[split_input[1]].name)
            print(f"You have picked up a {item[split_input[1]].name}!")

        elif split_input[0] == 'drop':
            player.drop_items(item[split_input[1]].name)
            print(f"You have dropped a {item[split_input[1]].name}.")
        
        else: 
            print("Please enter a valid command.")

    if len(split_input) == 1:

        if (user_input is 'n') and ((current_room_name in northlist) is True):
            print(f"""\n~~~~~~~~~~\n ⬆️  {player.name} is moving north, away from the {player.current_room}.""")
            player.current_room = room_object.n_to()

        elif user_input is 's' and ((current_room_name in southlist) is True):
            print(f"""\n~~~~~~~~~~\n ⬇️  {player.name} is moving south, away from the {player.current_room}.""")
            player.current_room = room_object.s_to()
            
        elif user_input is 'e' and ((current_room_name in eastlist) is True):
            print(f"""\n~~~~~~~~~~\n ➡️ {player.name} is moving east, away from the {player.current_room}.""")
            player.current_room = room_object.e_to()

        elif user_input is 'w' and ((current_room_name in westlist) is True):
            print(f"""\n~~~~~~~~~~\n ⬅️  {player.name} is moving west, away from the {player.current_room}.""")
            player.current_room = room_object.w_to()


# Add the i and inventory commands that both show a list of items currently carried by the player.
        elif user_input is 'i':
            print(f'{player.name} holds these items: {player.items}.')

        # If the user enters "q", quit the game.
        elif user_input is 'q':
            print("You are quitting the game")
            break

        


        elif user_input not in valid_list:
            print("Please input a valid direction (n,s,e,w)")

        # Print an error message if the movement isn't allowed.
        #  The parser should print an error if the player tries to move where there is no room.
        else:
            print("You cannot travel in this direction")
