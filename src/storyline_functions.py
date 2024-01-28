import logging
from random import randint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from functions import *
import os

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
        print('''\n\nYou have been selected for inter-galactic jury duty by the highest power in deep space...\n
        Despite all efforts, you can not wiggle out of this one...\n''')
        user_stats(stats["food"], stats["money"], stats["sanity"])
        input("press enter to continue...".center(110, " "))
        os.system("cls")
    elif choice == 1:
        print("There is a ship broken-down along the side of Desmos 9, do you want to help it?")
        user_choose = ""
        user_choose = input("\n[yes]\n[no]\n")
        options_list = ["yes", 'no']
        while user_choose.strip().lower() not in options_list:
            if user_choose.lower().strip() == "yes":
                dice_roll = randint(1, 6)
                logging.debug("the random number is %s", dice_roll)
                if dice_roll == 6:
                    print("""The ship was very grateful. All they needed was a quick jump.\n They rewarded 
                    you handsomely... + 1000 money""")
                    user_stats["money"] += 5000
                    user_stats(stats["food"], stats["money"], stats["sanity"])
                    input("press enter to continue...".center(110, " "))
                    os.system("cls")
                elif dice_roll == 1:
                    print("""The ship was full of pirates. It was a trap, they took half of everything\n
                    they took half of your sanity too.\n""")
                    user_stats(stats["food"], stats["money"], stats["sanity"])
                    input("press enter to continue...".center(110, " "))
                    os.system("cls")
                else:
                    print("""The ship did not want your help.. you continue on...""")
            elif user_choose.lower().strip() == "no":
                user_stats(stats["food"], stats["money"], stats["sanity"])
                input("press enter to continue...".center(110, " "))
                os.system("cls")
            else:
                print("Please type in either \n[yes]\nor\n[no]")
                user_choose = input()


    elif choice == 2:
        print("""You finally hit it big in the crypto^3 market despite having no idea what you are doing.\n
        collect some 2000 money which is 1000 after taxes""")
        stats["money"] += 1000
        user_stats(stats["food"], stats["money"], stats["sanity"])
        input("press enter to continue...".center(110, " "))
        os.system("cls")


random_event()
