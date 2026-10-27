# ********************************************************************
## age_validator.py       Author: Llewellyn (Cassie) VanDelinder
## Module 2: Assignment 1
# Demonstrates prompting for user input, validating, looping for retry, and case based response
# ********************************************************************

# -- INITIATE RETRY LOOP --
answered = False
while not answered:
    # -- PROMPT FOR AGE --
    AgeInput = input("Enter your age: ")

    # -- VERIFY IT'S A VALID RESPONSE, REPLY AND LOOP TO RE-PROMPT --
    try:
        Age = float(AgeInput)

        if Age < 10 or Age > 110:
            print("Umm...do you think I was born yesterday?  Try again!")
        else:
            answered = True
    except ValueError:
        print(f"Oops! '{AgeInput}' isn't a valid number. Try again")


# -- TEST IF AGE WITH DECIMAL GIVEN, CONVERT TO INTEGER --
PartialAge = not Age.is_integer()
Age = int(Age)

# -- RESPOND TO PARTIAL AGE (25.5, 23.2, ETC) WITH CHEEKY RESPONSE --
if PartialAge:
    print(
        f"A partial birthday? Really???  Let's go with '{Age}'. It's almost midnight!"
    )

# -- EVALUATE IF THEY PROBABLY GOT DYSYNTERY ON THE OREGON TRAIL OR NOT --
if Age >= 27:
    print(
        "     evaluating....  Ohhhh! You were born in the 1900s! How was the Oregon Trail?"
    )
else:
    print(
        f"     evaluating....   Wow! {Age} years old? At least you weren't born in the 1900s!"
    )
