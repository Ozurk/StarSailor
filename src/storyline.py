import logging
import os
from random import randint
from functions import *
import pprint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sleep_time = 0.2
stats = {"money": 10000, "sanity": 100, "food": 100}
inventory = {}
player_type = "[blank]"


def supervisor():
    user_stats()


def starvation():
    os.system("cls")
    print("It appears you ran out of food...\n")
    print("The only place to get food around here is the vending machine in the rest stop\nYou can pay 1000 for 10 food"
          "or you can beg for food from passerby\n")
    # if input == etc etc


def vending_machine():
    os.system("cls")
    print("welcome to the vending machine!\n")
    print("you have: " + str(stats["money"]) + " PD\n")
    food_purchase = input('10 packs of food cost 1000 PD\n\n\nhow much would you like '
                          'to purchase?\n[hint: enter a number]\n')
    food_number = number_regex(food_purchase)
    if len(food_number()) < 1:
        input("please enter a number")
        vending_machine()
    stats["money"] -= food_number * 1000
    stats["food"] += food_number * 10
    time.sleep(2)
    print('thank you for visiting :)')
    supervisor()




def intro_screen():
    # this is the fancy little intro screen
    typing_effect("-" * 115, .005)
    print()
    typing_effect("-" * 115, .005)
    print()
    typing_effect("-" * 115, .005)
    typing_effect("""  
             #####  #######    #    ######   #####     #    ### #       ####### ######  
            #     #    #      # #   #     # #     #   # #    #  #       #     # #     # 
            #          #     #   #  #     # #        #   #   #  #       #     # #     # 
             #####     #    #     # ######   #####  #     #  #  #       #     # ######  
                  #    #    ####### #   #         # #######  #  #       #     # #   #   
            #     #    #    #     # #    #  #     # #     #  #  #       #     # #    #  
             #####     #    #     # #     #  #####  #     # ### ####### ####### #     # """, .005)
    print("\n")
    typing_effect("-" * 115, .005)
    print()
    typing_effect("-" * 115, .005)
    print()
    typing_effect("-" * 115, .005)
    time.sleep(.75)
    print("\n" * 8)
    input("Press Enter to Continue...".center(115, " ") + "\n")
    print("\n")


def user_stats():
    items_list = ["food", 'money', 'sanity']
    iteration = 0
    print("-" * 115)
    print(('You are playing as: ' + player_type).center(115, " "))
    for items in items_list:
        print("-" * 115)
        print(((items_list[iteration]) + ": " + str(stats[items_list[iteration]])).center(115, " "))
        print("-" * 115)
        iteration += 1
    print("\n\n")
    input("press enter to contiue".center(115, "-") + "\n")
    os.system('cls')


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"), .005)
    print("\n" * 4)
    input("Press enter to play the game".center(115, "-") + "\n")
    user_stats()
    set_and_setting()


def set_and_setting():
    global player_type
    os.system("cls")
    typing_effect(get_file(r"storyline\chapter_1\setting and setup"), .005)
    player_type_options = ['1', '2', '3', '4']
    # make this a dictionary
    player_type = input("please enter one of the following:\n[1] sailor\n[2] scout\n[3] smuggler\n[4] scavver\n")
    while player_type not in player_type_options:
        player_type = input("please enter one of the following:\n[1] sailor\n[2] scout\n[3] smuggler\n[4] scavver\n")
    logging.debug("the player type is %s", player_type)
    player_type = player_type.lower().strip()
    if player_type == "1":
        player_type = 'sailor'
    elif player_type == "2":
        player_type = 'scout'
    elif player_type == "3":
        player_type = "smuggler"
    elif player_type == "4":
        player_type = 'scavver'
    user_stats()
    tunnel()


def tunnel():
    os.system("cls")
    typing_effect("""
    The Smokestacks are the colloquially named shanty-apartments residing above 
    The Foundry, the city's blazing furnace of manufactury. The choking smog is a perennial feat
    ure of your lodgings, but doesn't it seem particularly thick this evening?\n\n""", .000)
    input("Press enter to continue".center(115) + '\n')
    typing_effect(get_file(r"storyline//chapter_1/tunnel"), .000)
    tunnel_options = {"1": "option1", "2": "option2", "3": "option3"}
    tunnel_choice = input("\n")
    while tunnel_choice not in tunnel_options.keys():
        tunnel_choice = input("Please enter a\n[1]\n[2]\n[3]\n")
    if tunnel_choice == tunnel_options["1"]:
        print("option 1 ")
        # todo entrance_option_1()
    elif tunnel_choice == tunnel_options["2"]:
        print("Option 2")
        # todo entrance_option_2()
    elif tunnel_choice == tunnel_options["3"]:
        print("option 3")
        # todo entrance_option_3


# def entrance_option_1():
# todo

# def entrance_option_2():
# todo

# def entrance_option_1():
# todo

def random_event():
    os.system("cls")
    choice = randint(0, 2)
    if choice == 0:
        jury_duty()
    elif choice == 1:
        broken_down()
    elif choice == 2:
        crypto()


def jury_duty():
    typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
            Despite all efforts, you can not wiggle out of this one...\n
            You lose a little bit of your mind...''', 0)
    print('\n')
    print("-" * 115)
    input('Press Enter to Continue'.center(115))
    os.system("cls")
    stats["sanity"] -= 10
    stats["money"] += 10
    user_stats()


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


def broken_down():
    typing_effect("There is a ship broken-down along the side of Desmos 9, do you want to help it?".center(115), 0)
    print('\n')
    print("-" * 115)
    user_choose = yes_or_no("\ny[yes]\nor[no]\n")
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



vending_machine()
