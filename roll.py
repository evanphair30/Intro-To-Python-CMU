#Write a program to simulate randomly rolling two dice. Create a file called roll.py that can
#be executed in the following fashion:
#$ python roll.py
#Rolling dice...
#Die 1: 4
#Die 2: 3
#Total: 7

import random

print ("Rolling dice...")

def roll():
    min = 1
    max = 6
    dice1 = random.randint(min, max)
    print("Die 1:", dice1)
    dice2 = random.randint(min, max)
    print("Die 2:", dice2)
    usertotal = dice1 + dice2
    print("Total:", usertotal)
roll()




#Your output should be in the same format as shown above.
#You should create a function called roll(...) that executes your dice roll, and call this function from
#within your main script. You are free to design the inputs and outputs of this function as you wish. You
#must use the random module to randomly select the result of each dice roll.
#What to submit:
#You should upload a single file named roll.py
