# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # The Room class should be extended with a list that holds the Items that are currently in that room.
        self.room_item_list = []
    
    def __str__(self):
        return self.description

#   The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#   which point to the room in that respective direction.
    def n_to(self):
        if self.name == 'outside':
            self.name = 'foyer'
        elif self.name == 'foyer':
            self.name = 'overlook'
        elif self.name == 'narrow':
            self.name = 'treasure'
        return self.name
    
    def s_to(self):
        if self.name == 'foyer':
            self.name = 'outside'
        elif self.name == 'overlook':
            self.name = 'foyer'
        elif self.name == 'treasure':
            self.name = 'narrow'
        return self.name
         
    def e_to(self):
        if self.name == 'foyer':
            self.name = 'narrow'
        return self.name

    def w_to(self):
        if self.name == 'narrow':
            self.name = 'foyer'
        return self.name


    def add_items(self, item):
        self.item = item
        self.room_item_list.append(item)


    def display_items(self):
        return [item.name for item in self.room_item_list]

    # room_item_list = ['torch', 'rocks']
    # def print_item_list(self, room_item_list=room_item_list):
    #     self.room_item_list = room_item_list
    #     return room_item_list


