# Write a class to hold player information, e.g. what room they are in
# currently.

# * Put the Player class in `player.py`.
#   * Players should have a `name` and `current_room` attributes

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def drop_items(self, item):
        self.items.remove(item)

    def display_items(self):
        return [item.name for item in self.items]