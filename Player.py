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
  
  inventory = {
    "Item 1:" : wooden_spork_1,
    "Item 2:" : nothing,
    "Item 3:" : nothing,
    "Item 4:" : nothing,
    "Item 5:" : nothing
  }


  def inventory_list(self):
    for k, v in self.inventory.items():
      print(k, v.name)
  
  def manoeuvre():
    print("manoeuee!!")
  
  def fight(self, enemy):
    print("ATTACK:")


    slowprint("What would you like to attack with:")
    inventory_list()

    print("(input the number of the item you would like to use)")
    tool = int(input(":  "))

    


    
  def eat():
    print ("munch")
  
  def boon():
    print("splaboon")
  


  
  def update(self, enemy):
    action = int(input("What would you like to do?: \n1. Manoeuvre\n2. Fight\n3. Eat \n4. Boon"))

    if action == 1:
      self.manoeuvre()

    elif action == 2:
      self.fight()

    elif action == 3:
      self.eat()
      
    elif action == 4:
      self.boon()