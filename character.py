from item import Item

class Character(object):
    """
    Superclass for the characters, will not be used directly.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Enemy(Character):
    """
    A class for enemies
    """
    def __init__(self, name: str, description: str, health: int, damage: int, item: Item):
        super().__init__(name, description)
        self.health = health
        self.starthealth = health
        self.damage = damage
        self.item = item

    def attack(self):
        return self.damage

    def get_attacked(self, health: int):
        if self.health == self.starthealth:
            if self.name == 'Protector of the end of the game':
                print(f'{self.name} has is the final boos - beat them to win!')
            else:
                print(f'{self.name} has a {self.item.name}, defeat them to take it!')

        self.health -= health

        if self.health < 0:
            print('You defeated me!')
            item = self.item
            del self
            return item


class Friend(Character):
    """
    A class for Friends
    """
    def __init__(self, name: str, description:str, riddle:str, ans:str, item:Item):
        super().__init__(name, description)
        self.riddletext = riddle
        self.item = item
        self.ans = ans


    def riddle(self):
        if self.item:
            print(self.riddletext)
            answeruser = input(f"Can you solve {self.name}'s question? Type your answer\n >").lower()
            while answeruser != self.ans.lower():
                print('Not Quite - try again!')
                print(self.riddletext)
                answeruser = input(f"Can you solve {self.name}'s riddle? Type your answer\n >").lower()
            item = self.item
            self.item = None
            return item
        else:
            print("You've already got my item!")
            return None

