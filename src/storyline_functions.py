import logging
from random import randint
from functions import *
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


stats = {"money": 10000, "sanity": 100, "food": 100}


def chapter1a():
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\chapter1a"))
    # todo add something from here


def chapter1b():
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\chapter1b"))


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"))
    print("\n")
    storyline_splitter(one_or_two(), chapter1a(), chapter1b())


def random_event():
    os.system("cls")
    choice = randint(0, 2)
    logging.debug("the random number is %s", choice)
    if choice == 0:
        typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
        Despite all efforts, you can not wiggle out of this one...\n
        You lose a little bit of your mind...''')
        print('\n')
        print("-" * 110)
        input('Press Enter to Continue'.center(110))
        os.system("cls")
        stats["sanity"] -= 10
        user_stats(stats["food"], stats["money"], stats["sanity"])
        input("press enter to continue...".center(110, " "))
        os.system("cls")
    elif choice == 1:
        typing_effect("There is a ship broken-down along the side of Desmos 9, do you want to help it?".center(110))
        print('\n')
        print("-" * 110)
        user_choose = " "
        user_choose = input("\n[yes]\n[no]\n")
        options_list = ["yes", 'no']
        if user_choose.strip().lower() in options_list:
            if user_choose.lower().strip() == "yes":
                dice_roll = randint(1, 6)
                logging.debug("the dice roll is %s", dice_roll)
                if dice_roll == 6:
                    logging.debug("the number 6 option is running")
                    typing_effect("The ship was very grateful. All they needed was a quick jump.")
                    typing_effect("They rewarded you handsomely... + 5000 platinum disks")
                    print("-" * 110)
                    input('Press Enter to Continue'.center(110))
                    stats["money"] += 5000
                    user_stats(stats["food"], stats["money"], stats["sanity"])
                    input("press enter to continue...".center(110, " "))
                    os.system("cls")
                elif dice_roll == 1:
                    typing_effect("""The ship was full of pirates. It was a trap, they took half of everything\n""")
                    print("-" * 110)
                    input('Press Enter to Continue'.center(110))
                    os.system('cls')
                    stats["food"] *= .5
                    stats["sanity"] *= .5
                    stats["money"] *= .5
                    user_stats(stats["food"], stats["money"], stats["sanity"])
                    input("press enter to continue...".center(110, " "))
                    os.system("cls")
                else:
                    typing_effect("""The ship did not want your help.. you continue on...\n""")
                    print("-" * 110)
            elif user_choose.lower().strip() == "no":
                user_stats(stats["food"], stats["money"], stats["sanity"])
                input("press enter to continue...".center(110, " "))
                os.system("cls")
            else:
                print("Please type in either \n[yes]\nor\n[no]")

        elif user_choose not in options_list:
            input("Please enter\nyes\nor\nno")
            random_event()
            # goon
    elif choice == 2:
        typing_effect("You hit it big in the crypto^3 market despite having no idea "
                      "what you are doing.".center(110))
        print("\n")
        typing_effect("+ 2000 platinum disks".center(110))
        print('\n')
        print("-" * 110)
        print("\n")
        input('Press Enter to Continue'.center(110))
        stats["money"] += 1000
        os.system("cls")
        user_stats(stats["food"], stats["money"], stats["sanity"])
        print('\n')
        input("press enter to continue...".center(110, " "))
        os.system("cls")


while True:
    random_event()
