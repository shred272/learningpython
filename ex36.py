# defining variables
HaveMeat == False
HaveMoney == False

def outside():
    print("""You are drunk from partying and standing outside in a sandy plaza on Tatooine.
    Ahead of you, you see the notorious Mos Eisly Cantina bar where your favourite band plays.
    On your right, there is a local kebab shop.\n""")

    print("Where would you like to go?")

    choice = input("(bar/kebab)> ")

    if choice == "bar":
        cantina()
    elif choice == "kebab":
        kebab_shop()
    else:
        print("You can't make up your mind and drunkenly stumble around for a bit.\n")
        outside()


def kebab_shop():
    print("You enter the kebab shop where Gromodo greets you with a grunt.\n")

    if HaveMeat:
        print("Gromodo sniffs in your direction. Do you reveal the stolen meat to sell it?")

        choice = input("(yes/no)> ")

        if choice == "yes":
            print("""Gromodo grunts and you know he wants to buy the meat.
            You hand over the meat and he hands you a pouch of peggats much heavier than you expected.\n""")
        else:
            print("You let go a fart to conceal the meat smell and smile at Gromodo.\n")

    if HaveMoney:
        print("Do you want to buy kebab from Gromodo?")

        choice = input("(yes/no)> ")

        if choice == "yes":
            HaveMoney == False

            print("""You hand over your money and Gromodo gives you some kebab.
            "THIS IS THE BEST KEBAB EVER!" You drunkenly exclaim as you finish your food.
            You leave the shop.""")
            outside()
        else:
            print("""Gromodo yells at you to leave if you won't buy anything.
            You leave the shop.""")
            outside()
    else:
        print("You are too drunk and your head is spinning. You go back outside.")
        outside()

def cantina():
    print("""You enter the Mos Eisley Cantina and your favourite band is playing your favourite song!
    What a coincidence!
    You drunkenly dance for a bit and notice some swinging doors to the kitchen and at the other end of the room you see a door to going backstage.
    Where do you decide to go?""")
    choice = input("(outside/backstage/kitchen)> ")
    