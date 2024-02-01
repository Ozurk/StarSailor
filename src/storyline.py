import logging
import os
from random import randint
from time import sleep
from functions import *

sleep_time = 0.2


# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------This Prints Out the User Stats----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def user_stats():
    time.sleep(sleep_time)
    os.system('cls')
    print("\n" * 2)
    print("-" * 115)
    print(("You are a " + player_type + " player").center(115))
    print("-" * 115)
    print(('Inventory:' + str(inventory)).center(115))
    print("-" * 115)
    print(("Your Food Level is at " + str(stats["food"]) + "%").center(115))
    print("-" * 115)
    print(("You have " + str(stats["money"]) + " Platinum Disks").center(115))
    print("-" * 115)
    print(("Your Sanity is at " + str(stats["sanity"]) + "%").center(115))
    print("-" * 115)
    print("\n\n")
    print('-'*115)
    input("press enter to continue...".center(115, " "))
    os.system("cls")


# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------This Prints Out the User Stats----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------logging info------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------logging info------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------Variables--------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
stats = {"money": 10000, "sanity": 100, "food": 100}
inventory = []
player_type = "[blank]"


# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------Variables--------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------This is where the character gets set up-----------------------------------------
# -----------------------------------------------------------------------------------------------------------------


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"), .005)
    print("\n")
    input("Press enter to play the game".center(115, "-") + "\n")
    set_and_setting()


def set_and_setting():
    global player_type
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\setting and setup"), 0)
    # todo more text and more options
    player_type_options = ['sailor', 'scout', 'smuggler', 'scavver']
    player_type = input("please enter one of the following:\n[1] sailor\n[2] scout\n[3]smuggler\n[4]scavver\n")
    while player_type not in player_type_options:
        player_type = input("please enter one of the following:\n [1] sailor\n[2] scout\n[3]smuggler\n[4]scavver\n")
    # this is where the player will choose what they want to play as
    logging.debug("the player type is %s", player_type)
    player_type = player_type.lower().strip()
    if player_type == 1:
        player_type = player_type_options[0]
    elif player_type == player_type_options[1]:
        player_type = player_type_options[1]
    elif player_type == player_type_options[2]:
        player_type = player_type_options[2]
    elif player_type == player_type_options[3]:
        player_type = player_type_options[3]
    else:
        print("\nPlease type one of the options and try again\n")
        input("press enter to continue".center(115, " "))
    chapter_1()


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------This is where the character gets set up-----------------------------------------
# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------
# --------------------------------below is the first step to enter into the game-----------------------------------
# -----------------------------------------------------------------------------------------------------------------


def chapter_1():
    os.system("cls")
    typing_effect("""The Smokestacks are the colloquially named shanty-apartments residing above 
    The Foundry, the city's blazing furnace of manufactury. The choking smog is a perennial feat
    ure of your lodgings, but doesn't it seem particularly thick this evening?\n\n""", 0)
    input("Press enter to continue".center(115))
    typing_effect(get_file(r"storyline/chapter_1/chapter_1"), 0)



# -----------------------------------------------------------------------------------------------------------------
# --------------------------------above is the first step to enter into the game-----------------------------------
# -----------------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------
# --------------------------------here are the random events that can happen-------------------------------------
# ---------------------------------------------------------------------------------------------------------------
def random_event():
    os.system("cls")
    choice = randint(0, 2)
    if choice == 0:
        jury_duty()
    elif choice == 1:
        broken_down()
    elif choice == 2:
        crypto()



# ---------------------------------------------------------------------------------------------------------------
# --------------------------------here are the random events that can happen-------------------------------------
# ---------------------------------------------------------------------------------------------------------------


def jury_duty():
    typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
            Despite all efforts, you can not wiggle out of this one...\n
            You lose a little bit of your mind...''', 0)
    print('\n')
    print("-" * 115)
    input('Press Enter to Continue'.center(115))
    os.system("cls")
    stats["sanity"] -= 10
    user_stats()


def broken_down():
    typing_effect("There is a ship broken-down along the side of Desmos 9, do you want to help it?".center(115), 0)
    print('\n')
    print("-" * 115)
    user_choose = input("\n[yes]\n[no]\n")
    options_list = ["yes", "no"]
    while user_choose not in options_list:
        user_choose = input("please enter [yes] or [no]")

    if user_choose.strip().lower() in options_list:
        if user_choose.lower().strip() == "yes":
            dice_roll = randint(1, 6)
            logging.debug("the dice roll is %s", dice_roll)
            if dice_roll == 6:
                logging.debug("the number 6 option is running")
                typing_effect("The ship was very grateful.\nAll they needed was a quick jump.", 0)
                typing_effect("They rewarded you handsomely...\n + 5000 platinum disks\n", 0)
                print("-" * 115)
                input('Press Enter to Continue'.center(115) + "\n")
                stats["money"] += 5000
                user_stats()
                os.system("cls")
            elif dice_roll == 1:
                typing_effect("The ship was full of pirates. It was a trap, they took half of everything\n", 0)
                print("-" * 115)
                input('Press Enter to Continue'.center(115))
                os.system('cls')
                stats["food"] *= .5
                stats["sanity"] *= .5
                stats["money"] *= .5
                user_stats()
            else:
                typing_effect("""The ship did not want your help..\n you continue on...\n""", 0)
                print("-" * 115)
                user_stats()
        elif user_choose.lower().strip() == "no":
            user_stats()
        else:
            print("Please type in either \n[yes]\nor\n[no]")
            broken_down()


def crypto():
    typing_effect("You hit it big in the crypto^3 market despite having no idea "
                  "what you are doing.".center(115), 0)
    print("\n")
    typing_effect("+ 2000 platinum disks".center(115), 0)
    print('\n')
    print("-" * 115)
    print("\n")
    input('Press Enter to Continue'.center(115))
    stats["money"] += 1000
    os.system("cls")
    user_stats()

# -----------------------------------------------------------------------------------------------------------------
# ----------------------------Above are the functions within the random events ------------------------------------
# -----------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------
# --------------------------------------here is where the functions run-------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
intro_screen()

intro()
