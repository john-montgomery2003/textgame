
class Room():
    """
    A class for the rooms. This is for the
    """
    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.linked_rooms = {}
        self.character = None

    def describe(self):
        print('-'*40)
        print(f"{self.name} -> {self.description}" )
        if self.character:
            print('')
            print(f"{self.character.name}: {self.character.description}")
        print('')
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")
        print('-' * 40)

    def addcharacter(self, new_character):
        self.character = new_character

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self