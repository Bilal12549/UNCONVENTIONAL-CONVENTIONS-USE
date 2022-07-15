import time 
import replit
from termcolor import colored


from Player import *
from SlowPrint import *
from Monster import *

#--------------------------------------------------------------------------------#


slowprint("Welcome to Unconventional Conventions!", 0.1)

input("press enter")

replit.clear()

name = input("What is your name?: ")


inventory = {
  "item 1: ": "Wooden Spork",
  "item 2: ": ".",
  "item 3: ": ".",
  "item 4: ": ".",
  "item 5: ": ".",
}

replit.clear()

print("Inventory list:")
for k, v in inventory.items():
  print(k, v)

input("Press enter to continue")
replit.clear()

slowprint("Wait, Wait, Wait a minute minuite!", 0.1)
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

