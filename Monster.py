import random


class Monster():

  def __init__(self, name, fp, attack, abilities, ultimate):
    self.name = name
    self.fp = fp
    self.attack = attack
    self.ablities = abilities
    
    


  
  def update(self, player):
    ability_number = random.randint(0,3)
    ability_use = self.abilities[ability_number]
    player.hp -= self.abilities[ability_use]



class SmolBean(Monster):
  def __init__(self):
    Monster.__init__(self, "SmolBean", 40, random.randint(5,10), {"Mushy": 10, "Sugar snap": 7, "Vine wrap": 11}, {"Legumes in a pod" : 17})