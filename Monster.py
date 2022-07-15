import random


class Monster:
  def __init__(self):
    pass




class SmolBean(Monster):
  def __init__(self,
                name = "Smol Bean",
                hp= 5,
                atk= random.randint(1,3),
                ability = "Mushy"):

    self.name = name
    self.hp = hp
    self.atk = atk
    self.ability = ability


  def update():
    number = random.randint(1,10)
    