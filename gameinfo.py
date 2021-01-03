class gameinfo():
    """
    A class for info about the game
    """
    author = 'John'

    def __init__(self, gametitle):
        self.title = gametitle

    def welcome(self):
        print("Welcome to " + self.title)
        print('-'*40)
        print('Whilst playing there are a few commands you should know:')
        print('To attack the Enemy in the current room, use the command "attack')
        print('To speak to the Friend in the current room, use the command "speak')
        print('To heal (if you have the healing potion) use "heal"')
        print('To move, type the direction you want to move in')
        print('-' * 40)

    @classmethod
    def credits(cls):
        print("Thanks for playing")
        print("Created by " + cls.author)