

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def __str__(self):
    #      return self.name


# Call on_take method in Item. when the Item is picked up by the player.
# Implement support for the verb drop followed by an Item name. This is the opposite of get/take.
# The Item can use this to run additional code when it is picked up.
    def on_get(self):
        #print(f"You have picked up a {self.name!}")
        # player.add_items(item[split_input[1]].name)
        # print(f"You have picked up a {item[split_input[1]].name}!")
        pass

    def on_drop(self):
        #print(f"You have dropped a {self.name!}")
        pass