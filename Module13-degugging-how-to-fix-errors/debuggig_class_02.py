'''
REPRODUCE THE B UG
Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

PAUSE 1
Change the code so that it always produces the occasional error.

PAUSE 2
Fix the code and remove the bug.
'''
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6) - original, the list goes from  0 - 5, not 1-6

#PAUSE 1
#Change the code so that it always produces the occasional error.
#dice_num = randint(6, 8)

#PAUSE 2
#Fix the code and remove the bug.
dice_num = randint(0,5)
print(dice_images[dice_num])