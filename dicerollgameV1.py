# Dice Roller Script 
# Created by Shreyas
# Date: July 4th 2025

import random
import time

print(" Welcome to Dice Roller Game")

input("Press Enter to roll the die... ")

print("Rolling...", end=" ")
time.sleep(1)
print()
dice = random.randint(1, 6)
print(" You rolled a " +  str(dice)  + "!")
print("Thanks for rolling! ! !")
