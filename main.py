import time 
import replit
from termcolor import colored

from Fight import *
from Monster import *
from Player_items import *
from Player import *
from SlowPrint import *
#--------------------------------------------------------------------------------#


slowprint("Welcome to Unconventional Conventions!", 0.1)
input("press enter")
replit.clear()



name = input("What is your name?: ")

if name == "billyboy125":
  player  = Player(name, 100000, 20000)
else:
  player = Player(name, 100, 20)

replit.clear()



print("Inventory list:")
player.inventory_list()



input("Press enter to continue")
replit.clear()

slowprint("Wait, Wait, Wait a minute minute! (the first minute: as in 'mineute' as in small).", 0.1)
time.sleep(0.5)

slowprint("Was that a wooden spork!?", 0.1)
time.sleep(0.5)

slowprint("How terrible.", 0.1)
time.sleep(0.5)

slowprint("Mabye try to pick a more effective instrument in future, eh?", 0.1)
time.sleep(0.5)

slowprint("Press enter to continue into the game. . . . .", 0.1)
input("")

replit.clear()
#--------------------------------------------------------------------------------#


while player.hp >= 0:
  SBean_1 = SmolBean()
  fight(player, SBean_1, "you win!")
