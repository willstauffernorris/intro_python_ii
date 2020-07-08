# Implement a class to hold room information. This should have name and
# description attributes.



# * Put the Room class in `room.py` based on what you see in `adv.py`.

#   * The room should have `name` and `description` attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.description

    def n_to(self, name):
        self.name = name
        if name == 'outside':
            #global name
            name = 'foyer'


# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']