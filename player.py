from character import Enemy
from item import Item


class Player(object):
    """
    A class for the player - including if they die
    """
    def __init__(self):
        self.name = input('Enter the name of your player\n > ')
        self.inventorylist = []
        self.health = 100

    def inventory(self, newitem: Item):
        if newitem.name != 'Stick':
            print(f"You got {newitem.name} - it was added to your inventory")
        self.inventorylist.append(newitem)

    def getattacked(self, enemy: Enemy):
        print(f"You were attacked by {enemy.name} - you lost {enemy.damage}")
        self.health -= enemy.damage
        if self.health <= 0:
            print("You died")
            print("""   ____                         ___                 _ 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)""")
            return 'endgame'
        else:
            print(f"New health - {self.health}")
