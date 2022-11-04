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
    print("MANOUEE:")
  
  def fight(self, enemy):
    print("ATTACK:")

    print("What would you like to attack with:")
    self.inventory_list()

    print("(Input the number of the item you would like to use)")
    tool = int(input(":  "))
    tool -= 1
    tool_use = self.inventory[tool]

    print(tool_use.damage_message)

    enemy.hp -= tool_use.damage


    
  def eat(self):
    print("Es hora de COMER:")

    print("what would you like to eat:")
    self.inventory_list()

    print("(Input the number of the item you would like to eat)")
    food = int(input(":  "))
    food -= 1
    food_use = self.inventory[food]

    print(food_use.heal_message)

    self.hp += food_use.heal

    
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