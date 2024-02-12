import logging
import os
from random import randint
import shutil
from functions import *
from random import randint
import pyautogui

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
sleep_time = 0.00
stats = {"money": 10000, "sanity": 100, "food": 100}
inventory = {}
player_variable = "[blank]"

terminal_width = shutil.get_terminal_size().columns


# ----------------------------------------------------------------------------------------------------------------------
def supervisor():
    os.system("cls")
    user_stats()
    if stats["food"] <= 0:
        starvation()
    if stats["sanity"] <= 0:
        insane()
    if stats['money'] <= 0:
        beg()
    if randint(1, 5) == 1:
        random_event()


def insane():
    print("you lost your mind")
    input("press enter to continue...\n")
    counter = 0
    while counter != 5:
        try:
            pyautogui.screenshot(r"..\pictures\screenshot.png")
            cmd_x = pyautogui.locateCenterOnScreen(r"..\pictures\closeout_cmd.png", grayscale=True)
            print(cmd_x)
            pyautogui.moveTo(cmd_x[0], cmd_x[1], 3)
            time.sleep(.25)
            pyautogui.click()
        except pyautogui.ImageNotFoundException:
            print("You are trying to close the instance of your game")
            counter += 1
    input("There was a cool way the game was suppose to work, but it did not work properly...\n press enter to quit")
    death()


def starvation():
    os.system("cls")
    print("-" * terminal_width)
    print("-" * terminal_width)
    print("It appears you have no food...".center(terminal_width, " "))
    if stats['money'] < 1000:
        beg()
    print("-" * terminal_width)
    print("-" * terminal_width)
    print('you can press your luck begging for money [1]'.center(terminal_width, " "))
    print("-" * terminal_width)
    if stats["money"] > 100:
        print("or you can visit the vending machine to buy some more food [2]".center(terminal_width, " "))
    print("-" * terminal_width)
    print("-" * terminal_width)
    user_picks = one_or_two()
    if user_picks == 1:
        beg()
    elif user_picks == 2:
        vending_machine()
    else:
        print("Please report this to Hunter if you see this...Something has malfunctioned...")
    print("-" * terminal_width)


def vending_machine():
    os.system("cls")
    print("welcome to the vending machine!\n")
    print("you have: " + str(stats["money"]) + " PD\n\n")
    print("100 PD for 10 food\n")
    food_quantity = stats["money"] // 1000
    print("you can buy up to: [" + str(food_quantity) + ']\n')
    food_number = number_regex(
        input("enter the the amount of food you want to purchase".center(terminal_width, '-') + "\n"))
    stats["money"] -= (food_number * 100)
    stats["food"] += (food_number * 1)
    time.sleep(2)
    print('thank you for visiting :)'.center(terminal_width, ' '))


def beg():
    print("-" * terminal_width)
    print("-" * terminal_width)
    print("You ran out of food and money, and you are loosing your sanity quickly...")
    input("you are sitting outside of the rest-stop with a sign begging for money.")
    print("-" * terminal_width)
    while stats["money"] < 100:
        spinner(randint(1, 5))
        d10_die = randint(1, 30)
        if d10_die == 1:
            input("The stranger was kind and gave you 1000 PD, you can now visit the vending machine.")
            stats["money"] += 1000
            vending_machine()
        elif d10_die == 10:
            input("The stranger killed you")
            death()
        elif 11 < d10_die < 20:
            donation = randint(1, 300)
            print('The stranger gave you ' + str(donation) + " PD")
            stats['money'] += donation
            if stats["sanity"] < 100:
                stats["sanity"] += 1
            print("you have " + str(stats["money"]) + " PD")
            print("your sanity is at " + str(stats["sanity"]) + "%")
        else:
            print("The stranger passed by, pretending not to notice you")
            stats["sanity"] -= 5
            print("you have " + str(stats["money"]) + " PD")
            print("your sanity is at " + str(stats["sanity"]) + "%")
        if stats["sanity"] < 0:
            insane()
    vending_machine()


def user_stats():
    items_list = ["food", 'money', 'sanity']
    iteration = 0
    print("-" * terminal_width)
    print(('You are playing as: ' + player_variable).center(terminal_width, " "))
    for items in items_list:
        print("-" * terminal_width)
        print(((items_list[iteration]) + ": " + str(stats[items_list[iteration]])).center(terminal_width, " "))
        print("-" * terminal_width)
        iteration += 1
    print("\n\n")


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"), sleep_time)
    print("\n" * 4)
    input("Press enter to play the game".center(terminal_width, "-") + "\n")
    set_and_setting()


def set_and_setting():
    os.system("cls")
    typing_effect(get_file(r"storyline\setup\setting and setup"), sleep_time)
    tunnel()


def tunnel():
    os.system("cls")
    typing_effect("""
    The Smokestacks are the colloquially named shanty-apartments residing above 
    The Foundry, the city's blazing furnace of manufactury. The choking smog is a perennial feat
    ure of your lodgings, but doesn't it seem particularly thick this evening?\n\n""", .000)
    typing_effect(get_file(r"src/storyline/setup/tunnel"))
    heavens_forge()


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
    print("-" * 175)
    input('Press Enter to Continue'.center(terminal_width))
    os.system("cls")
    stats["sanity"] -= 10
    stats["money"] += 10


def crypto():
    typing_effect("You hit it big in the crypto^3 market despite having no idea "
                  "what you are doing.".center(terminal_width), 0)
    print("\n")
    typing_effect("+ 1750 platinum disks".center(terminal_width), 0)
    print('\n')
    print("-" * 175)
    print("\n")
    input('Press Enter to Continue'.center(terminal_width))
    stats["money"] += 1000
    os.system("cls")


def broken_down():
    typing_effect("There is a ship broken-down along the side of Desmos 9, do you wan"
                  "t to help it?".center(terminal_width), 0)
    print('\n')
    print("-" * 175)
    user_choose = yes_or_no("\ny[yes]\nor[no]\n")
    if user_choose.lower().strip() == "yes":
        dice_roll = randint(1, 6)
        logging.debug("the dice roll is %s", dice_roll)
        if dice_roll == 6:
            logging.debug("the number 6 option is running")
            typing_effect("The ship was very grateful.\nAll they needed was a quick jump.", 0)
            typing_effect("They rewarded you handsomely...\n + 5000 platinum disks\n", 0)
            print("-" * 175)
            input('Press Enter to Continue'.center(terminal_width) + "\n")
            stats["money"] += 5000
            os.system("cls")
        elif dice_roll == 1:
            typing_effect("The ship was full of pirates. It was a trap, they took half of everything\n", 0)
            print("-" * 175)
            input('Press Enter to Continue'.center(terminal_width))
            os.system('cls')
            stats["food"] *= .5
            stats["sanity"] *= .5
            stats["money"] *= .5
        else:
            typing_effect("""The ship did not want your help..\n you continue on...\n""", 0)
            print("-" * 175)


def death():
    typing_effect(get_file(r"storyline\endgame\death"), sleep_time)
    input("Press Enter to quit...".center(terminal_width, "-"))
    quit()
    # todo add a better death screen


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 1-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_1():
    supervisor()
    print("this is task 1")
    input("return to location_1")
    # todo rename this
    heavens_forge()


def heavens_forge():
    supervisor()
    typing_effect(get_file(r"storyline/location_1/Heaven's Forge"), sleep_time)
    print("You have 3 options:\n[1] do task 1\n[2] Go to location 7\n[3] go to twilight isles")
    choice = one_through_3()
    if choice == 1:
        task_1()
    elif choice == 2:
        location_7()
    elif choice == 3:
        twilight_isles()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 2-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_2():
    supervisor()
    print("this is task 2")
    input('return to twilight isles')
    task_2()


def twilight_isles():
    supervisor()
    typing_effect(get_file(r"storyline/location_2/Twilight Isles"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_2()
    elif choice == 2:
        location_3()
    elif choice == 3:
        heavens_forge()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 3-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_3():
    supervisor()
    print("this is task 3")
    input('return to location 3')
    location_3()


def location_3():
    supervisor()
    typing_effect(get_file(r"storyline/location_3/location3"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_3()
    elif choice == 2:
        location_4()
    elif choice == 3:
        twilight_isles()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 4-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_4():
    supervisor()
    print("this is task 4")
    input('return to location 4')
    location_4()


def location_4():
    supervisor()
    typing_effect(get_file(r"storyline/location_4/location4"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_4()
    elif choice == 2:
        location_5()
    elif choice == 3:
        location_3()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 5-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_5():
    supervisor()
    print("this is task 5")
    input('return to location 5')
    location_5()


def location_5():
    supervisor()
    typing_effect(get_file(r"storyline/location_5/location5"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_5()
    elif choice == 2:
        location_6()
    elif choice == 3:
        location_4()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 6-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_6():
    supervisor()
    print("this is task 5")
    input('return to location 5')
    location_6()


def location_6():
    supervisor()
    typing_effect(get_file(r"storyline/location_6/location6"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_6()
    elif choice == 2:
        location_7()
    elif choice == 3:
        location_5()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 6-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_7():
    supervisor()
    print("this is task 7")
    input('return to location 7')
    location_7()


def location_7():
    supervisor()
    typing_effect(get_file(r"storyline/location_7/location7"), sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_7()
    elif choice == 2:
        heavens_forge()
    elif choice == 3:
        location_6()


# ----------------------------------------------------------------------------------------------------------------------

intro_screen()
intro()
