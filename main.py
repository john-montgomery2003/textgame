from player import Player
from character import Enemy, Friend
from room import Room
from item import Item
from gameinfo import gameinfo



# First set up the info and present the welcome
info = gameinfo('an OOP game')
info.welcome()

# Set up all the rooms...
kitchen = Room(
    'Kitchen',
    'Its the kitchen! Maybe youll find something here...'
)

dining = Room(
    'Dining Room',
    'This is where people eat i guess'
)

office = Room(
    'Office',
    'People do work here - maybe theres a code in here?'
)

living = Room(
    'Living Room',
    'Is there someone in here?'
)

secret = Room(
    'Secret Room',
    'Secret room, must be something hidden in here...'
)

hallway = Room(
    'Hallway',
    'Just a hallway'
)

vault = Room(
    'Vault',
    'For all the valuables'
)

# Now we link all the rooms, each room is linked - so they can all be accessed
dining.link_room(kitchen, 'S')
kitchen.link_room(dining, 'N')

dining.link_room(hallway, 'W')
hallway.link_room(dining, 'E')

living.link_room(hallway, 'S')
hallway.link_room(living, 'N')

office.link_room(hallway, 'E')
hallway.link_room(office, 'W')

office.link_room(secret, 'S')
secret.link_room(office, 'N')

vault.link_room(secret, 'N')
secret.link_room(vault, 'S')

# Set up a player
player = Player()

# Set up the items that will be interacted with
health = Item(
    'Health Potion',
    'Restores health',
    'health'
)

stick = Item(
    'Stick',
    'Beat your enemy to death with a stick',
    'weapon',
    damage=20
)

# The user gets this weapon by default
player.inventory(stick)

sword = Item(
    'Sword',
    'Its a sword',
    'weapon',
    damage=30
)

newtonsflaminglasersword = Item(
    'Newtons Flaming Laser Sword',
    'Its Newtons Flaming Laser Sword!',
    'weapon',
    damage=100
)

key1 = Item(
    'Key 1',
    'The 1st key! now to find the lock...',
    'key',
    room = office
)

key2 = Item(
    'Key 2',
    'The 2nd key! now to find the lock...',
    'key',
    room = vault
)

key3 = Item(
    'Key 3',
    'The 3rd key! now to find the lock...',
    'key',
    room = secret
)

newton = Friend(
    'Issac Newton',
    'The famous guy',
    'Whats the value of g on earth?',
    '9.8',
    newtonsflaminglasersword
)

# Now for all the enemies...

somerandomguy = Friend(
    'Some Random Guy',
    'Just someone in your house i guess. At least they are friendly',
    'What goes up but never comes down?',
    'age',
    key3
)

octopus = Enemy(
    'Octopus',
    'PUT OCTOPUS DESCRIPTION HERE',
    10,
    10,
    health
)

guard = Enemy(
    'Guard',
    'Someone has to look after the office!',
    100,
    20,
    sword
)

guyintheoffice = Enemy(
    'Guy in the Office',
    'just someone in the office apparently',
    10,
    1,
    key1
)

cook = Enemy(
    'The cook',
    'idk its the cook',
    100,
    40,
    key2
)

finalbossdude = Enemy(
    'Protector of the end of the game',
    '< as the name says - probably dont want to fight without the laser sword here!',
    400,
    20,
    None
)

# Put each character in a room
kitchen.character = cook
office.character = guyintheoffice
secret.character = guard
hallway.character = somerandomguy
dining.character = newton
living.character = octopus
vault.character = finalbossdude


# Set the players current
currentroom = hallway
dead = False
while not dead:
    currentroom.describe()
    userchoice = input(" > ")

    # If the user decides to move
    if userchoice in ['N','S','W','E']:
        # Entry to the secret rooms needs all 3 keys
        if currentroom == secret:
            if key1 not in player.inventorylist or key2 not in player.inventorylist or key3 not in player.inventorylist\
                    and userchoice.lower() == 's':
                print('You dont have all the keys yet! explore some more...')
            else:
                currentroom = currentroom.move(userchoice)
        else:
            currentroom = currentroom.move(userchoice)



    # If they decide to attack an enemy
    elif userchoice.lower() == 'attack':
        if isinstance( currentroom.character , Enemy):
            dead = player.getattacked(currentroom.character)
            damage = 0
            for item in player.inventorylist:
                if item.type == 'weapon':
                    damage = max(damage, item.damage)
            itemtoadd = currentroom.character.get_attacked(damage)
            if itemtoadd:
                currentroom.character = None
                player.inventory(itemtoadd)
        else:
            print('This isnt an enemy!')

    # If they decide to speak to a friend
    elif userchoice.lower() == 'speak':
        if isinstance(currentroom.character, Friend):
            item = currentroom.character.riddle()
            player.inventory(item)
        else:
            print('This isnt a friend! Attack!')
    elif userchoice.lower() == 'heal':

        if health in player.inventorylist:
            player.health = 150
            print('You healed')
        else:
            print('You dont have this item yet...')

    # If they defeat the final player
    if currentroom == vault and currentroom.character.health <1:
        print(""" __   __           __        ___       _ 
 \ \ / /__  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)""")


#Run the credits
gameinfo.credits()
exit()