import random
import sys
from time import sleep
incoming ="INCOMING....MESSAGE....AGENT Q...."
ruthere ="ARE YOU THERE?...Y/N"
mission ="""
YOU HAVE BEEN TASKED WITH A TOP SECRET MISSION TO FOIL THE PURCHASE OF SOME BLACK MARKET RUBBER CHICKENS

WHEN YOU ARRIVE AT THE PARK, LOOK AT YOUR SUPPORTING AGENTS TO CHECK WHETHER THE DEAL IS ON OR OFF

USE THE CHECKLIST BELOW BEFORE ENTERING THE PARK OTHERWISE YOUR POSITION MAY BE COMPROMISED

THE DEAL IS ON IF ONE OF THE FOLLOWING ARE TRUE:

•	ANDY DOESN’T BUY AN ICE CREAM AND CHRIS SITS UNDER AN UMBRELLA

•	BETH DOESN'T DRINK A MILKSHAKE AND CHRIS SITS UNDER AN UMBRELLA

•	CHRIS DOESN’T SIT UNDER AN UMBRELLA AND DAVINA DOESN'T WEAR SUNGLASSES

•	ANDY BUYS AN ICE CREAM, BETH DRINKS A MILKSHAKE AND CHRIS DOESN'T SIT UNDER AN UMBRELLA

YOU HAVE YOUR MISSION

GOODLUCK AGENT Q

"""

wdplan = """
WELL DONE AGENT Q YOU HAVE MANAGED TO IDENTIFY WHEN THE DEAL WAS TAKING PLACE AND FOILED THEIR PLANS

TILL NEXT TIME....

"""

gameover = """
AGENT Q... YOU HAVE FAILED THE MISSION, BLOWN OUR COVER AND COMPROMISED ALL OF OUR AGENTS
RETURN YOUR EQUIPMENT AND AWAIT DEBREIFING...
"""


wdnoplan = """
AGENT Q WE HAVE NOT MANAGED TO FOIL THEIR PLANS BUT AT LEAST WE DID NOT BLOW OUR COVER

"""

Andy = ["hasn't bought an ice cream", "bought an ice cream"]
Beth = ["not drinking anything", "drinking a milkshake"]
Chris = ["nowhere near an umbrella", "sitting under an umbrella"]
Davina = ["wearing reading glasses", "wearing sunglasses"]





destruction="THIS MESSAGE WILL SELF-DESTRUCT IN 5..4..3..2..1..."

for a in incoming:
    print(a, end="", flush=True); sleep(0.01)

print()

for a in ruthere:
    print(a, end="", flush=True); sleep(0.01)

print()
response = input().upper()

if response == "Y":
    for a in mission:
        print(a, end="", flush=True); sleep(0.01)

    andychoice = random.randint(0,1)
    bethchoice = random.randint(0,1)
    chrischoice = random.randint(0,1)
    davinachoice = random.randint(0,1)

    print("You have arrived at the park")
    print("You see Agent Andy {}".format((Andy[andychoice])))
    print("You see Agent Beth {}".format((Beth[bethchoice])))
    print("You see Agent Chris {}".format(Chris[chrischoice]))
    print("You see Agent Davina {}".format(Davina[davinachoice]))

    deal = input("Agent Q is the deal on? Y/N \n").upper()

    if deal == "Y" and andychoice == 0 and chrischoice == 1:
        for a in welldone:
            print(a, end="", flush=True); sleep(0.01)
            
    elif deal == "Y" and bethchoice == 0 and chrischoice == 1:
        for a in welldone:
            print(a, end="", flush=True); sleep(0.01)

    elif deal == "Y" and chrischoice == 0 and davinachoice == 0:
        for a in welldone:
            print(a, end="", flush=True); sleep(0.01)

    elif deal == "Y" and andychoice == 1 and bethchoice == 1 and chrischoice == 0:
        for a in welldone:
            print(a, end="", flush=True); sleep(0.01)
            
    elif deal == "Y":
        for a in gameover:
            print(a, end="", flush=True); sleep(0.01)
    else:
        for a in ohno:
            print(a, end="", flush=True); sleep(0.01)
        for a in destruction:
            print(a, end="", flush=True); sleep(0.01)
    
else:
    for a in destruction:
        print(a, end="", flush=True); sleep(0.1)



