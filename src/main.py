import logging
from functions import *
from random import randint
import pyautogui

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class DeveloperControls:
    sleep_time = 0.00  # delay between letters in typing effect
    def __init__(self):
        pass



class Player:
    def __init__(self):
        pass

    stats = {"money": 10000, "sanity": 100.00, "food": 100.00}
    inventory = {"oranges": 6}
    gameplay = True
    planets_visited = {"chevron_ii": False, "Sweetrain Planet": False, "Acropolis": False,
                       "wormwood planet": False, "mars": False, "cobaltiania": False, "B-IRS": False}


class Ship:
    inventory = {"oranges": 5}
    health = 100.0
    crew = {}
    type = ""

    def __init__(self):
        pass


def change_inventory():
    user_choice = yes_or_no(input("Transfer items to or from ship inventory?\n[yes]\n[no]\n"))
    if user_choice == 'yes':
        add_ship_inventory()
    elif user_choice == 'no':
        pass


def add_ship_inventory():
    while True:
        user_choice = input("\nWhat would you like to add to your ship's inventory?\n".lower().strip())
        user_choice_quantity = input("how many would you like to add to the ships inventory\n?")
        try:
            if int(user_choice_quantity) <= Player.inventory[user_choice]:
                Player.inventory[user_choice] -= int(user_choice_quantity)
                Ship.inventory[user_choice] += int(user_choice_quantity)
                supervisor()
                break
            else:
                print("\nyou can only transfer the amount of [" + user_choice + "]s that are in your inventory.\n")
        except TypeError:
            print("please enter a number\n")


terminal_width = shutil.get_terminal_size().columns


# ----------------------------------------------------------------------------------------------------------------------
def supervisor():
    os.system("cls")
    user_stats()
    if Player.gameplay:
        if Player.stats["food"] <= 0:
            starvation()
        if Player.stats["sanity"] <= 0:
            insane()
        if Player.stats['money'] <= 0:
            beg()
        if randint(1, 5) == 1:
            random_event()
    input("Press enter to continue...".center(terminal_width) + "\n")


def insane():
    print("you lost your mind")
    input("press enter to continue...\n")
    counter = 0
    while counter != 5:
        try:
            pyautogui.screenshot(r"..\pictures\screenshot.png")
            cmd_x = pyautogui.locateCenterOnScreen(r"..\pictures\closeout_cmd.png", grayscale=True)
            print(cmd_x)
            pyautogui.moveTo(cmd_x[0], cmd_x[1], 4)
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
    if Player.stats['money'] < 1000:
        beg()
    print("-" * terminal_width)
    print("-" * terminal_width)
    print('you can press your luck begging for money [1]'.center(terminal_width, " "))
    print("-" * terminal_width)
    if Player.stats["money"] > 100:
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
    print("you have: " + str(Player.stats["money"]) + " PD\n\n")
    print("100 PD for 10 food\n")
    food_quantity = Player.stats["money"] // 1000
    print("you can buy up to: [" + str(food_quantity) + ']\n')
    food_number = number_regex(
        input("enter the the amount of food you want to purchase".center(terminal_width, '-') + "\n"))
    Player.stats["money"] -= (food_number * 100)
    Player.stats["food"] += (food_number * 1)
    time.sleep(2)
    print('thank you for visiting :)'.center(terminal_width, ' '))


def beg():
    print("-" * terminal_width)
    print("-" * terminal_width)
    print("You ran out of food and money, and you are loosing your sanity quickly...")
    input("you are sitting outside of the rest-stop with a sign begging for money.")
    print("-" * terminal_width)
    while Player.stats["money"] < 100:
        spinner(randint(1, 5))
        d10_die = randint(1, 30)
        if d10_die == 1:
            input("The stranger was kind and gave you 1000 PD, you can now visit the vending machine.")
            Player.stats["money"] += 1000
            vending_machine()
        elif d10_die == 10:
            input("The stranger killed you")
            death()
        elif 11 < d10_die < 20:
            donation = randint(1, 300)
            print('The stranger gave you ' + str(donation) + " PD")
            Player.stats['money'] += donation
            if Player.stats["sanity"] < 100:
                Player.stats["sanity"] += 1
            print("you have " + str(Player.stats["money"]) + " PD")
            print("your sanity is at " + str(Player.stats["sanity"]) + "%")
        else:
            print("The stranger passed by, pretending not to notice you")
            Player.stats["sanity"] -= 5
            print("you have " + str(Player.stats["money"]) + " PD")
            print("your sanity is at " + str(Player.stats["sanity"]) + "%")
        if Player.stats["sanity"] < 0:
            insane()
    vending_machine()


def user_stats():
    items_list = ["food", 'money', 'sanity']
    iteration = 0
    print("-" * terminal_width)
    for items in items_list:
        print("-" * terminal_width)
        print(((items_list[iteration]) + ": " + str(Player.stats[items_list[iteration]])).center(terminal_width, " "))
        print("-" * terminal_width)
        iteration += 1
    print(("Player.inventory: " + str(Player.inventory)).center(terminal_width))
    print("\n\n")


def intro():
    os.system("cls")
    typing_effect(get_file(r".\storyline\intro"), DeveloperControls.sleep_time)
    print("\n" * 4)
    input("Press enter to play the game".center(terminal_width, "-") + "\n")
    set_and_setting()


def set_and_setting():
    os.system("cls")
    typing_effect(get_file(r".\storyline\setup\setting and setup"), DeveloperControls.sleep_time)
    tunnel()


def tunnel():
    os.system("cls")
    typing_effect(get_file(r".\storyline\setup\tunnel"), DeveloperControls.sleep_time)
    input("Press enter to continue...\n")
    heavens_forge()


def ssin_validatator():
    Player.gameplay = False
    while True:
        print("-" * terminal_width)
        print("Sanity:" + str(Player.stats["sanity"]))
        print("-" * terminal_width)
        ssin = input("Please Enter 8 digits.\n").strip()
        if len(ssin) != 8:
            input("The number you entered is not long enough.\nPlease try again...\n")
            return
        elif not ssin.isdigit():
            print("The text you provided raised a #VALUE error.\nPlease try again...\n")
            return
        odd_numbers = ssin[1::2]
        for digits in odd_numbers:
            if float(digits) % 2 == 0:
                Player.stats["sanity"] -= .5
                print("The number you entered was not valid.\n"
                      "The number that caused an error was: " + digits + "\n")
                Player.stats["sanity"] *= .99
                return
        even_numbers = ssin[::2]
        for even_digits in even_numbers:
            if float(even_digits) % 2 != 0:
                print("The number you entered was not valid.\n"
                      "The number that caused an error was: " + even_digits + "\n")
                Player.stats["sanity"] *= .99
                return
        typing_effect("\nThank you for visiting the Flagstaff BMV.\n Have a great day!", DeveloperControls.sleep_time)
        input("\nPress enter to continue...")







def rems_event():
    Player.gameplay = False
    os.system("cls")
    typing_effect("Your ships registration has expired\n", DeveloperControls.sleep_time)
    time.sleep(2)
    typing_effect("You must report to the nearest BMV to update your registration.\nThe nearest "
                  "spaceship certified BMV is in Flagstaff Arizona, USA, Earth, Solar System,"
                  " Milky Way Galaxy.\n", DeveloperControls.sleep_time)
    print("\n\n")
    input("Press Enter to continue".center(terminal_width) + "\n")

    typing_effect("you arrived at BMV Flagstaff 48 minutes ago, the line"
                  " seems to be crawling by...\n", DeveloperControls.sleep_time)

    spinner(6)
    os.system("cls")
    typing_effect("\nFinally, your number is called. "
                  "you approach the clerk's desk and sit down.\n", DeveloperControls.sleep_time)
    time.sleep(4)
    os.system("cls")
    typing_effect("You are informed you must provide a 16 digit \"SPACESHIP IDENTIFICATION NUMBER\"",
                  DeveloperControls.sleep_time)
    typing_effect("\nYou do not have the original bill of sale for the ship"
                  " and heavens know that every board on this ship has been replaced. The original SSIN "
                  "is nowhere to be found.\n\n", DeveloperControls.sleep_time)
    time.sleep(4)
    os.system("cls")
    print("You must now provide an SSIN that passes the validation tests.".center(terminal_width))
    print("\n")
    print('There are some criteria that must be met, but you can\'t seem to remember them!'.center(terminal_width))
    print("\n")
    input("Press enter to continue...".center(terminal_width) + "\n")
    ssin_validatator()
    Player.gameplay = True


def random_event():
    os.system("cls")
    choice = randint(0, 3)
    if choice == 0:
        jury_duty()
    elif choice == 1:
        broken_down()
    elif choice == 2:
        crypto()
    elif choice == 3:
        rems_event()


def jury_duty():
    typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
            Despite all efforts, you can not wiggle out of this one...\n
            You lose a little bit of your mind...''', 0)
    print('\n')
    print("-" * terminal_width)
    input('Press Enter to Continue'.center(terminal_width))
    os.system("cls")
    Player.stats["sanity"] -= 10
    Player.stats["money"] += 10
    supervisor()


def crypto():
    typing_effect("You hit it big in the crypto^3 market despite having no idea "
                  "what you are doing.".center(terminal_width), 0)
    print("\n")
    typing_effect("+ 1750 platinum disks".center(terminal_width), 0)
    print('\n')
    print("-" * terminal_width)
    print("\n")
    input('Press Enter to Continue'.center(terminal_width))
    Player.stats["money"] += 1000
    os.system("cls")
    supervisor()


def broken_down():
    typing_effect("There is a ship broken-down along the side of Desmos 9, do you wan"
                  "t to help it?".center(terminal_width), 0)
    print('\n')
    print("-".center(terminal_width, "-"))
    user_choose = yes_or_no("\ny[yes]\nor[no]\n")
    if user_choose.lower().strip() == "yes":
        dice_roll = randint(1, 6)
        logging.debug("the dice roll is %s", dice_roll)
        if dice_roll == 6:
            logging.debug("the number 6 option is running")
            typing_effect("The ship was very grateful.\nAll they needed was a quick jump.", 0)
            typing_effect("They rewarded you handsomely...\n + 5000 platinum disks\n", 0)
            print("-" * terminal_width)
            input('Press Enter to Continue'.center(terminal_width) + "\n")
            Player.stats["money"] += 5000
            os.system("cls")
        elif dice_roll == 1:
            typing_effect("The ship was full of pirates. It was a trap, they took half of everything\n", 0)
            print("-" * terminal_width)
            input('Press Enter to Continue'.center(terminal_width))
            os.system('cls')
            Player.stats["food"] *= .5
            Player.stats["sanity"] *= .5
            Player.stats["money"] *= .5
        else:
            typing_effect("""The ship did not want your help..\n you continue on...\n""", 0)
            print("-" * terminal_width)
    supervisor()


def death():
    typing_effect(get_file(r"storyline\endgame\death"), DeveloperControls.sleep_time)
    input("Press Enter to quit...".center(terminal_width, "-"))
    quit()
    # todo add a better death screen


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 1-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_1():
    supervisor()
    typing_effect(get_file(r"storyline/Heaven's Forge/LightWelder"), DeveloperControls.sleep_time)
    input("return to Heaven's Forge")
    # todo rename this
    heavens_forge()


def heavens_forge():
    supervisor()
    typing_effect(get_file(r"storyline/Heaven's Forge/Heaven's Forge Intro"), DeveloperControls.sleep_time)
    print("You have 3 options:\n[1] do task 1\n[2] Go to location 7\n[3] go to twilight isles")
    choice = one_through_3()
    if choice == 1:
        task_1()
    elif choice == 2:
        location_7()
    elif choice == 3:
        planet_sweetrain()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 2-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_2():
    supervisor()
    print("this is task 2")
    input('return to twilight isles')
    task_2()


def planet_sweetrain():
    supervisor()
    typing_effect(get_file(r"storyline/Twilight Isles/Twilight Isles intro"), DeveloperControls.sleep_time)
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
    typing_effect(get_file(r"storyline/location_3/loamstone"), DeveloperControls.sleep_time)
    print("""IN FUTURE VISITS TO ACROPOLIS, YOU MAY NOW TRAVEL TO LOAMSTONE!
    The Reticent Rancher will allow you to gather your own mushrooms, where you may brave the dark and spores to refill your
    galley. You will net +10 Food for -2 Sanity. This deal is useful if you're sound of mind but low on foodstuffs.

    [1] Return to the plow wagon - Back to city, your crew, your ship.
    [2] Harvest Some Mushrooms
    """)
    Player.inventory['dreamcap'] = 1
    input('')
    location_3()


def location_3():
    supervisor()
    typing_effect(get_file(r"storyline/Acropolis/Acropolis"), DeveloperControls.sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_3()
    elif choice == 2:
        location_4()
    elif choice == 3:
        planet_sweetrain()


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
    typing_effect(get_file(r"storyline/location_4/Wormwood Planet"), DeveloperControls.sleep_time)
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
    typing_effect(get_file(r"storyline/location_5/Mars"), DeveloperControls.sleep_time)
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
    typing_effect(get_file(r"storyline/location_6/Cobatiania"), DeveloperControls.sleep_time)
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
    typing_effect(get_file(r"storyline/location_7/B-IRS"), DeveloperControls.sleep_time)
    choice = one_through_3()
    if choice == 1:
        task_7()
    elif choice == 2:
        heavens_forge()
    elif choice == 3:
        location_6()


# ----------------------------------------------------------------------------------------------------------------------
ssin_validatator()
