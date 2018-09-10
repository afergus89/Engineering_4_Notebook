# Automatic Dice Roller
# Written by Molly and Alex

from random import randint

print ("Automatic Dice Roller")
response = ""

while response == "":
    response = input("press enter to roll or x then enter to quit")
    from random import randint
    if response == "x":
        print("")
    else:
        print(randint(0,6))



