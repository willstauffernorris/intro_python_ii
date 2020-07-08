# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.description
#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.
# room['outside'].n_to = room['foyer']
    def n_to(self, name):
        self.name = name
        if self.name == 'outside':
            #global name
            self.name = 'foyer'
    def __str__(self):
        return self.name
            



# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']