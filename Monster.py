import random

class Monster():

  def __init__(self, name, hp, attack, ability):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.ability = ability

    def update(player):
      pass



class SmolBean(Monster):
  def __init__(self):
    Monster.__init__(self, "SmolBean", 100, 20, "Mushy")
    