# ********************************************************************
## LostHollow_Adventure.py       Author: Llewellyn (Cassie) VanDelinder
## Module 2: Assignment 1
#  A nostalgic re-visit of text based adventure games
#  Demonstrates INPUT & STRIP, UPPERCASE, TRANSFORM - REVERSE, EXCEPTION HANDLING, CALCULATE AREA FROM RADIUS, ANALYSIS/STRING SPLIT
# ********************************************************************

import time
import math

# -- SET VARIABLES --
health = 100


# -- SCENE: WELCOME AND GREETING --
print("WELCOME traveler to the Lost Hollow Lodge")
time.sleep(3)
print("where the beds are lumpy and the food is terrible.")
time.sleep(3)
print("<the keeper eyes you warily and mutters a great 'harumph'>")
time.sleep(3)
TravelerName = input("What is your name, traveler? ").strip()  # [DEMO: INPUT & STRIP]

SCENE_Greeting = [
    f"{TravelerName.title()}. Odd name that is...though we don't get many come through here. <the keeper looks anxiously at the door trying to hurry him along.>",
    "<the now agitated keeper rummages under the counter>",
    f"Here TAKE THIS {TravelerName.upper()}! The innkeeper says",  # [DEMO: UPPERCASE]
    "as he drops a crusty hunk of bread on the counter.",
    "'Uh....closing time...here...you must go...now...away with you!",
]

for line in SCENE_Greeting:
    print(line)
    time.sleep(4)


# -- PROMPT FOR BREAD CHOICE --
print(
    "The bread rests beside the lantern. Do you take the bread or leave it? (Type 'take' or 'leave')"
)
BreadChoice = input(">").strip().lower()
if BreadChoice == "take":
    print(
        "You grab the bread and stuff it into your pack. The innkeeper looks at you with a mixture of disgust and fear. 'Good luck out there!' he says as he shuffles to the door."
    )
elif BreadChoice == "leave":
    print(
        "You leave the bread on the counter. The innkeeper looks at you with a mixture of disgust and fear. 'Good luck out there!' he says as he shuffles to the door."
    )
else:
    print(
        "The hunk of bread, hard as a stone, rolls off the counter and onto your foot. "
    )
    print("OUCH!\nYou lose 5 health points.")
    health = health - 5
    print(f"{health} health points remaining.")


# -- SCENE: LEAVE THE INN --

time.sleep(3.5)

SCENE_LeaveInn = [
    "You shuffle foot to foot, wondering why the innkeeper became so agitated.",
    "'Ummm...thanks?' you reply halfheartedly, taking one small step towards the door.",
    "The innkeeper makes a facepalming motion, warring against his better judgement",
    "He JUMPS IN FRONT OF YOU - cutting off your exit!",
    "He leans over, his bad breath nearly making you gag, and whispers into your ear....",
    f"The code word...is......{TravelerName[::-1].upper()}. Just a slight pause and he is gone.",  # [DEMO: TRANSFORM - REVERSE]
    "'Holy cow, batman!' You think to yourself.",
]

for line in SCENE_LeaveInn:
    print(line)
    time.sleep(4)

# -- SCENE: EXPLORE THE TOWN --

time.sleep(3.5)
print(
    "You step out into the sunshine and take great gulping breaths...muttering mouthwash under your breath"
)

SCENE_Explore = [
    "Behind you, the door snaps shut, ringing with the final sound of a lock snapping in place.",
    "Whelp. Can't go back in there, you think, eying the brick wall in front of you.",
    "Nope. Maybe in my younger days...you think to yourself, glancing down the street",
    "A woman suddenly appears out of thin air!",
    "You jump backwards, barely catching yourself.",
    "'Why...you look a little lost, dearie' she croons with a menacing grin",
    "'How far were you planning to walk today?' she asks",
    "'What an odd question', you think, then give a shrug, pondering your answer",
]

for line in SCENE_Explore:
    print(line)
    time.sleep(4)

# -- PROMPT FOR TRAVEL RADIUS AND CALCULATE AREA--

print(
    'She looks at you expectantly. "How many miles will you travel?"\nEnter a number from 1 to 8.'
)

answered = False
while not answered:
    RadiusInput = input(">").strip()

    try:  # [DEMO: EXCEPTION HANDLING]
        radius = float(RadiusInput)
        if radius < 1:
            print("Are you really that tired? you can at LEAST walk 1 mile! Try again")
        elif radius > 8:
            print("Pace yourself! Rome wasn't built in a day! Try again")
        else:
            answered = True
    except ValueError:
        print(
            f"The math just isn't mathing! '{RadiusInput}' isn't a number from 1 to 8! Umm...it's not even a number! Try again"
        )

area = math.pi * radius**2  # [DEMO: USE CASE - AREA OF A CIRCLE]

# -- SCENE: The Escape--

time.sleep(2)

SCENE_Escape = [
    f"That is {area:.2f} square miles to get lost in....",
    "Your breath catches as her mouth spreads into an inhuman grin",
    "and her eyes begin to glow red.",
    "Not to worry, dearie...I will show you the way....",
    "'Umm....no....err...no....thank..you', you stammer",
]

for line in SCENE_Escape:
    print(line)
    time.sleep(3)

FinalSentence = "I can find my own way... BYE!"
print(FinalSentence)
words = FinalSentence.replace(".", "").upper().split()  # [DEMO: ANALYSIS/STRING SPLIT]

for word in words:
    print(word)
    time.sleep(1.5)
