import random

class Player:

  def manoeuvre():
    print("manoeuee!!")
  
  def fight():
    print("FIGHT")
    
  def eat():
    print ("munch")
  
  def boon():
    print("splaboon2")

    
  def __init__(self, name, inventory, hp=100, atk=100):

    self.name = name
    self.hp = hp
    self.atk = atk
    self.inventory = inventory
  
  
  

  def update(self, enemy):
    action = input("""What would you like to do?: \n1. Manoeuvre\n2. Fight\n3. Eat \n4. Boon""")

    if action == 1:
      self.manoeuvre()

    elif action == 2:
      self.fight()

    elif action == 3:
      self.eat()
      
    elif action == 4:
      self.boon()

      
  def manoeuvre():
    print("manoeuee!!")
  
  def fight():
    print("FIGHT")
    
  def eat():
    print ("munch")
  
  def boon():
    print("splaboon2")