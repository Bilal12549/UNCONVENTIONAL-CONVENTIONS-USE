import random

class Monster():

  def __init__(self, name, hp, attack, ability):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.ability = ability

    def update(self, player):
      pass






class SmolBean(Monster):
  def __init__(self):
    Monster.__init__(self, "SmolBean", 40, random.randint(5,10), "Mushy")
    