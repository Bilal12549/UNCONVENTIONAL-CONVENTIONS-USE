import random


class Player:
    def __innit__(self, name, inventory, hp=100, atk=100):

        self.name = name
        self.hp = hp
        self.atk = atk
        self.inventory = inventory

    def update(enemy):
        action = input("""What would you like to do?:
                                                1. Manoeuvre
                                                2. Fight
                                                3. Eat
                                                4. Boon""")

        def manoeuvre():
            pass

        def fight():
            pass

        def eat():
            pass

        def boon():
            pass

        if action == 1:
            manoeuvre()

        elif action == 2:
            fight()

        elif action == 3:
            eat()

        elif action == 4:
            boon()
