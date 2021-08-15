# these will be used as global variables throughout
HaveMeat = False
HaveMoney = False

def outside():
    print("You are drunk from partying and you are standing outside in a sandy plaza on Tatooine.")
    print("Ahead of you, you see the notorious Mos Eisly Cantina bar where your favourite band plays.")
    print("On your right, there is a local kebab shop.\n")

    print("Where would you like to go?")

    choice = input("(bar/kebab)> ")

    if choice == "bar":
        print("You head to the Mos Eisley Cantina.")
        cantina()
    elif choice == "kebab":
        print("You head to the kebab shop.")
        kebab_shop()
    else:
        print("You can't make up your mind and drunkenly stumble around for a bit.\n")
        outside()

def kebab_shop():
    global HaveMeat
    global HaveMoney
    print("You enter the kebab shop where Gromodo greets you with a grunt.\n")
    if HaveMeat:
        print("Gromodo sniffs in your direction. Do you reveal the stolen meat to sell it?")

        choice = input("(yes/no)> ")

        if choice == "yes":
            HaveMeat = False
            print("Gromodo grunts and you know he wants to buy the meat.")
            print("You hand over the meat and he hands you a pouch of peggats much heavier than you expected.\n")
            HaveMoney = True
        else:
            print("You let go a fart to conceal the meat smell and smile at Gromodo.\n")
#   we have 2 IF statements so both can be processed individually
    if HaveMoney:
        print("Do you want to buy kebab from Gromodo?")

        choice = input("(yes/no)> ")

        if choice == "yes":
            HaveMoney = False

            print("You hand over your money and Gromodo gives you some kebab.")
            print('"THIS IS THE BEST KEBAB EVER!" You drunkenly exclaim as you finish your food.')
            print("You leave the shop.")
            outside()
        else:
            print("Gromodo yells at you to leave if you won't buy anything.")
            print("You leave the shop.")
            outside() 
    else:
        print("You are too drunk and your head is spinning. You go back outside.")
        outside()

def cantina():
    print("You enter the Mos Eisley Cantina and your favourite band is playing your favourite song!")
    print("What a coincidence!")
    print("You drunkenly dance for a bit and notice some swinging doors to the kitchen and at the other end of the room you see a door to going backstage.")
    print("Where do you decide to go?")
    choice = input("(outside/backstage/kitchen)> ")

    if choice == "outside":
        print("You leave the building.")
        outside()
    elif choice == "backstage":
        print("You head to the door that leads backstage.")
        backstage()
    elif choice == "kitchen":
        print("You head through the swinging doors that lead into the kitchen.")
        kitchen()
    else:
        print("You are too drunk and get thrown out of the building.")
        outside()

def backstage():
    global HaveMoney
    print("You enter a corridor and can see the entrance to go backstage but it is blocked by a large bouncer.")
    print("The bouncer sees you and tells you to get lost.")

    if HaveMoney:
        print("Do you bribe the bouncer with the large pouch of peggats?")
        choice = input("(yes/no)> ")
        if choice == "yes":
            print("You reach for the pouch of peggats and throw it to the bouncer. The bouncer looks at it in disbelief and let's you pass.")
            print("CONGRATULATIONS! You got to meet your favourite band and have some drinks with them!")
            exit(0)
        else:
            print("You leave the corridor and go back in the bar.")
            cantina()
    else:
        print("You leave the corridor and go back in the bar.")
        cantina()

def kitchen():
    global HaveMeat
    print("You enter the kitchen where everyone is too busy to worry about you.")
    print("You see a stash of high quality prime meat. Do you steal some meat?")

    choice = input("(yes/no)> ")

    if (choice == "yes") and HaveMeat:
        print("You are already carrying some of the stolen meat.")
        print("You leave the kitchen.")
        cantina()
    elif (choice == "yes") and (HaveMeat == False):
        print("You quickly steal some meat, put it in your coat, and rush out the door.")
        HaveMeat = True
        cantina()
    else:
        print("You take a look around and decide to leave.")
        cantina()

outside()