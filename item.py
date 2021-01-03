

class Item(object):

    def __init__(self, name, description, type, room=None, damage=None):
        self.name = name
        self.description = description
        self.type = type
        self.room = room
        self.damage = damage


    def use(self, player):
        if self.type == 'weapon':
            print(f"{player.name} attacks with {self.name}")
            return self.damage
        elif self.type == 'key':
            print(f"{player.name} gave you the key to {self.room}")
        else:
            return
