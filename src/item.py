

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

# The Item can use this to run additional code when it is picked up.
    def on_get(self):
        print(f"You have picked up a {self.name!}")

    def on_drop(self):
        print(f"You have dropped a {self.name!}")