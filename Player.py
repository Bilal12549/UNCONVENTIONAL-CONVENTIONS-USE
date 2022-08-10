import random
from SlowPrint import *
from Player_items import *

class Player:
  
  def __init__(self, name, hp, atk):

    self.name = name
    self.hp = hp
    self.atk = atk



  
  wooden_spork_1 = wooden_spork()
  nothing = nothing()
  
  inventory = [
    wooden_spork_1,
    nothing,
    nothing,
    nothing,
    nothing
  ]


  def inventory_list(self):
    for i in range(len(self.inventory)):
      print(f"Item {i+1}: {self.inventory[i].name}")




  
  def manoeuvre(self):
    print("manoeuee!!")
  
  def fight(self, enemy):
    print("ATTACK:")


    print("What would you like to attack with:")
    self.inventory_list()

    print("(input the number of the item you would like to use)")
    tool = int(input(":  "))
    tool -= 1
    tool_use = self.inventory[tool]

    slowprint(tool_use.damage_message, 0.1)

    enemy.hp -= tool_use.damage


    
  def eat(self):
    print ("munch")
  
  def boon(self):
    print("boonito")
  





  
  def update(self, enemy):
    action = int(input("What would you like to do?: \n1. Manoeuvre\n2. Fight\n3. Eat \n4. Boon"))

    if action == 1:
      self.manoeuvre(enemy)

    elif action == 2:
      self.fight(enemy)

    elif action == 3:
      self.eat(enemy)
      
    elif action == 4:
      self.boon(enemy)