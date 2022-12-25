import random


class Monster():

  def __init__(self, name, hp, attack, abilities_d, abilities_l, ultimate_d, ultimate_l, ability1_msg, ability2_msg, ability3_msg, ultimate_msg):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.ablities_d = abilities_d
    self.abilities_l = abilities_l
    self.ultimate_d = ultimate_d
    self.ultimate_l = ultimate_l
    self.ability1_msg = ability1_msg
    self.ability2_msg = ability2_msg
    self.ability3_msg = ability3_msg
    self.ultimate_msg = ultimate_msg


  def update(self, player):
    ability_ultimate_b = False
    ability_ultimate_number = random.randint(0,100)
    
    if ability_ultimate_number >= 85:
      ability_ultimate_b = True
      ultimate_name = self.ultimate_l[0]
      ultimate_use = self.ultimate_d[ultimate_name]
      player.hp -= ultimate_use
      print(self.ultimate_msg)
      
      

    if ability_ultimate_b == False:
      ability_number = random.randint(0,3)
      ability_name = self.abilities_l[ability_number]
      ability_use = self.abilities_d[ability_name]
      player.hp -= ability_use
      if ability_number == 0:
        print(self.ability1_msg)
      if ability_number == 1:
        print(self.ability2_msg)
      if ability_number == 2:
        print(self.ability3_msg)


      
class SmolBean(Monster):
  def __init__(self):
    Monster.__init__(self, "SmolBean", 40, random.randint(5,10), {"Mushy": 10, "Sugar snap": 7, "Vine wrap": 11}, ["Mushy", "Sugar snap", "Vine wrap"], {"Legumes in a pod" : 17}, ["Legumes in a pod"], "The SmolBean uses mushy. You have been mushified. You nor smolbean knows what this means. It deals 10 damage...", "SNAP, you have been sugared! SmolBean attcks with valiance trying its very best :) It deals a mere 7 damage.", "Smol bean calls upon its old pea pod plant and orders for its vines to entrap you. Seeing this makes you want to go awwh. Regradless, it deals a hefty 11 damage.", "Hark! what is this... SmolBean sees you are a tough oponent and uses its most powerful attck. It beckons its siblings from its very own mother pea plant and they fly toward you. As they valiantly try to help their dear brother they DIE TRYING... This does no inital damage to you however seeing this pointless effort in vein gives you a feeling of emptiness. It deals 17 EMOTIONAL DAMAGE (Note: EMOTIONAL DAMAGE works the same as normal damage).")