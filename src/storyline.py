import logging
from random import randint
from functions import *
import os

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------logging info------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------Variables--------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
stats = {"money": 10000, "sanity": 100, "food": 100}
inventory = []
player_type = ""
# -----------------------------------------------------------------------------------------------------------------
# ------------------------------------here are the actual story chapters-------------------------------------------
# -----------------------------------------------------------------------------------------------------------------


def chapter1a():
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\chapter1a"), 0)
    # todo more text and more options
    chapter1a_options = ['sailor', 'scout', 'smuggler', 'scavver']
    player_type_choice = input("\n[sailor]\n[scout]\n[smuggler]\n[scavver]")







def chapter1b():
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\chapter1b"), 0)


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"), 0)
    print("\n")
    input("Press enter to play the game".center(110, "-"))
    chapter1a()


# ---------------------------------------------------------------------------------------------------------------
# --------------------------------here are the random events that can happen-------------------------------------
# ---------------------------------------------------------------------------------------------------------------
def random_event():
    os.system("cls")
    choice = randint(0, 2)
    logging.debug("the random number is %s", choice)
    if choice == 0:
        typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
        Despite all efforts, you can not wiggle out of this one...\n
        You lose a little bit of your mind...''', 0)
        print('\n')
        print("-" * 110)
        input('Press Enter to Continue'.center(110))
        os.system("cls")
        stats["sanity"] -= 10
        user_stats(stats["food"], stats["money"], stats["sanity"])
        input("press enter to continue...".center(110, " "))
        os.system("cls")
    elif choice == 1:
        typing_effect("There is a ship broken-down along the side of Desmos 9, do you want to help it?".center(110), 0)
        print('\n')
        print("-" * 110)
        user_choose = input("\n[yes]\n[no]\n")
        options_list = ["yes", 'no']
        if user_choose.strip().lower() in options_list:
            if user_choose.lower().strip() == "yes":
                dice_roll = randint(1, 6)
                logging.debug("the dice roll is %s", dice_roll)
                if dice_roll == 6:
                    logging.debug("the number 6 option is running")
                    typing_effect("The ship was very grateful. All they needed was a quick jump.", 0)
                    typing_effect("They rewarded you handsomely... + 5000 platinum disks", 0)
                    print("-" * 110)
                    input('Press Enter to Continue'.center(110))
                    stats["money"] += 5000
                    user_stats(stats["food"], stats["money"], stats["sanity"])
                    input("press enter to continue...".center(110, " "))
                    os.system("cls")
                elif dice_roll == 1:
                    typing_effect("""The ship was full of pirates. It was a trap, they took half of everything\n""", 0)
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
                    typing_effect("""The ship did not want your help.. you continue on...\n""", 0)
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
                      "what you are doing.".center(110), 0)
        print("\n")
        typing_effect("+ 2000 platinum disks".center(110), 0)
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


# -----------------------------------------------------------------------------------------------------------------
# --------------------------------------here is where the functions run-------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

time.sleep(1)
intro_screen(0)
intro()
