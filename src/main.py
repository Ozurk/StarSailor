import logging
import time
import pandas
from functions import *
from random import randint
import pyautogui
from reset_tables import reset_tables
import sys

# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------Settings and Controls-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
terminal_width = shutil.get_terminal_size().columns


class DeveloperControls:
    sleep_time = 0.03  # delay between letters in typing effect

    def __init__(self):
        pass


class Player:
    stats = {"money": 10000, "sanity": 0, "food": 100.00}
    inventory = {}
    gameplay = False
    planets_visited = {"intro": True, "heavens forge": True, "twilight isles": True, "acropolis": True,
                       "loamstone": True,
                       "wormwood planet": True, "mars": True, "cobaltiania": True, "B-IRS": True, }
    on_board = []

    def __init__(self):
        pass


def user_stats():
    items_list = ["food", 'money', 'sanity']
    iteration = 0
    print("-" * terminal_width)
    for items in items_list:
        print("-" * terminal_width)
        print(
            ((items_list[iteration]) + ": " + str(Player.stats[items_list[iteration]])).center(terminal_width, " "))
        print("-" * terminal_width)
        iteration += 1
    print(("Inventory: " + str(Player.inventory)).center(terminal_width, " "))
    print("-" * terminal_width)
    print(str(Player.on_board).center(terminal_width))
    print("-" * terminal_width)
    print("\n\n")


def supervisor():
    os.system("cls")
    Player.stats['food'] -= 1
    if Player.gameplay:
        if Player.stats["food"] <= 0:
            starvation()
        if Player.stats['sanity'] <= 0:
            insane()
        if Player.stats['money'] <= 0:
            beg()
        if randint(1, 15) == 1:
            random_event()
    user_stats()


def gameplay_speed(location):
    if Player.planets_visited[location]:
        DeveloperControls.sleep_time = .00
    else:
        DeveloperControls.sleep_time = .03


# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------------Consequences and Menu----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

def insane():
    print("you lost your mind")
    input("press enter to continue...\n")
    # todo make a better inanity screen
    while True:
        pyautogui.moveRel(10, -10, .02)
        sys.stdout.write("all work and no play makes Jack a dull boy.")


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


def death():
    typing_effect(get_file(r"storyline\endgame\death"), DeveloperControls.sleep_time)
    input("Press Enter to quit...".center(terminal_width, "-"))
    quit()
    # todo add a better death screen


def broken_down():
    typing_effect("There is a ship broken-down along the side of Desmos 9, do you wan"
                  "t to help it?".center(terminal_width), DeveloperControls.sleep_time)
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
            input("\n")
    supervisor()


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------Random Events-----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


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


def ssin_validatator():
    print("-" * terminal_width)
    print("Sanity:" + str(Player.stats["sanity"]))
    print("-" * terminal_width)
    ssin = input("Please Enter 8 digits.\n").strip()
    if len(ssin) != 8:
        input("The number you entered is not long enough.\nPlease try again...\n")
        return
    if not ssin.isdigit():
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
    return ssin


def ssin_function():
    while True:
        if ssin_validatator() is not None:
            break


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
    ssin_function()
    print("Thank you for visiting BMV flagstaff Arizona.\nHave a nice day...\n")
    Player.gameplay = True


def jury_duty():
    supervisor()
    typing_effect('''You have been selected for inter-galactic jury duty by the highest power in deep space...\n
            Despite all efforts, you can not wiggle out of this one...\n
            You lose a little bit of your mind...''', DeveloperControls.sleep_time)
    print('\n')
    print("-" * terminal_width)
    input('Press Enter to Continue'.center(terminal_width))
    os.system("cls")
    Player.stats["sanity"] -= 10
    Player.stats["money"] += 100


def crypto():
    supervisor()
    typing_effect("You hit it big in the crypto^3 market despite having no idea "
                  "what you are doing.".center(terminal_width), 0)
    print("\n")
    typing_effect("+ 1750 platinum disks".center(terminal_width), 0)
    print('\n')
    print("-" * terminal_width)
    print("\n")
    input('Press Enter to Continue'.center(terminal_width))
    Player.stats["money"] += 1000


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------Pandas Functions-----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def item_getter(csv, row_choice):
    try:
        int(row_choice)
    except ValueError:
        print("Please only enter numbers\n")
        return
    if row_choice == "":
        return
    table = pandas.read_csv(csv)
    try:
        row = table.iloc[int(row_choice)]
    except IndexError:
        print("Please enter the index number of the item you want to purchase.\n")
    row_as_dict = row.to_dict()
    print("Purchase " + row["ITEM NAME"] + " for " + str(row["PRICE"]) + "PD?\n")
    choose = yes_or_no(input("[yes] or [no]\n"))
    if choose != "yes":
        return
    if row["PRICE"] <= Player.stats["money"]:
        Player.stats['money'] -= int(row_as_dict["PRICE"])
        if row_as_dict["RESOURCE"] == 'food':
            Player.stats['food'] += int(row_as_dict['AMOUNT'])
        elif row_as_dict['RESOURCE'] == 'sanity':
            Player.stats['sanity'] += int(row_as_dict['AMOUNT'])
        elif row_as_dict['RESOURCE'] == 'money':
            Player.stats['money'] += int(row_as_dict['AMOUNT'])
        else:
            Player.inventory[row_as_dict["ITEM NAME"]] = row_as_dict["AMOUNT"]
        table = table.drop(int(row_choice), axis=0)
        table.to_csv(csv, index=False)
    else:
        print("you do not have enough money to purchase this item.")
        time.sleep(2)


# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------Intro, Setup and Menu-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def intro():
    if not Player.planets_visited["intro"]:
        supervisor()
        typing_effect(get_file(r".\storyline\intro"), DeveloperControls.sleep_time)
        print("\n" * 4)
        input("press enter to proceed".center(terminal_width) + "\n")
        set_and_setting()


def set_and_setting():
    supervisor()
    typing_effect(get_file(r".\storyline\setup\Setup and Help"), DeveloperControls.sleep_time)
    print("\n")
    print("-" * terminal_width)
    input("\n\nBefore you start, lets do a little training\nPress enter to continue.")
    supervisor()
    print("\nFor this exercise, you must purchase the [ruby].")
    time.sleep(2)
    typing_effect("\nA merchant is selling some items. Select what you want to purchase,\n"
                  "or press enter to skip \n", DeveloperControls.sleep_time)
    print("-" * terminal_width)
    table_printer("tables\\setup.csv")
    user_input = input()
    user_input = user_input.strip()
    while user_input != '1':
        print("\n[Remember, you must purchase the [ruby]]\n")
        time.sleep(1)
        user_input = input("\n")
    Player.inventory['ruby'] = 1
    Player.stats["money"] -= 1000
    print("a ruby has been added to your inventory\n")
    Player.planets_visited["intro"] = True


def tunnel():
    os.system("cls")
    typing_effect(get_file(r".\storyline\setup\tunnel"), DeveloperControls.sleep_time)
    input("Press enter to continue...\n")
    Player.gameplay = True
    heavens_forge_landing()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 1-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def heavens_forge_market():
    supervisor()
    market = pandas.read_csv(r"tables/heaven's forge market.csv")
    print(market)
    user_input = input("\n enter the ID of the item you would like to purchase, or press enter to leave...\n")
    item_getter(r"tables/heaven's forge market.csv", user_input.strip())
    heavens_forge_landing()


def task_1():
    supervisor()
    if 'starpaint' in Player.inventory.keys():
        typing_effect(get_file(r"storyline/Heaven's Forge/Lightwelder[starpaint]"), DeveloperControls.sleep_time)
        input("Press enter to continue\n")
        Player.inventory['hardlight'] = True
        Player.inventory.pop('starpaint', None)

    else:
        typing_effect(get_file(r"storyline/Heaven's Forge/LightWelder"), DeveloperControls.sleep_time)
    input("\n")
    heavens_forge_landing()


def heavens_forge_landing():
    supervisor()
    Player.gameplay = False
    gameplay_speed("heavens forge")
    Player.planets_visited["heavens forge"] = True
    typing_effect(get_file(r"storyline/Heaven's Forge/Heaven's Forge Landing"), DeveloperControls.sleep_time)
    choice = number_validation(5)
    if choice == 1:
        task_1()
    elif choice == 2:
        Player.gameplay = True
        location_7()
    elif choice == 3:
        Player.gameplay = True
        twilight_isles_landing()
    elif choice == 4:
        heavens_forge_market()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 2-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def sun_seared_navigator():
    supervisor()
    typing_effect(get_file(r"storyline/Twilight Isles/roasted navigator"), DeveloperControls.sleep_time)
    choice = int(number_validation(3))
    if choice == 1:
        Player.on_board.append("Sun Seared Navigator")
        acropolis()
    elif choice == 2:
        twilight_isles_landing()


def twilight_isles_market():
    supervisor()
    print("Welcome to to Twilight Isles Floating Market".center(terminal_width))
    print("\n")
    market = pandas.read_csv("tables/twilight isles market.csv")
    print(market)
    user_input = input("\nenter the ID of the item you would like to purchase, or press enter to leave...\n")
    item_getter(r"tables/twilight isles market.csv", user_input.strip())
    twilight_isles_landing()


def twilight_isles_landing():
    supervisor()
    Player.gameplay = False
    gameplay_speed("twilight isles")
    Player.planets_visited["twilight isles"] = True
    typing_effect(get_file(r"storyline/Twilight Isles/Twilight Isles landing"), DeveloperControls.sleep_time)
    print("\n")
    choice = number_validation(5)
    if choice == 1:
        sun_seared_navigator()
    elif choice == 2:
        twilight_isles_market()
    elif choice == 3:
        Player.gameplay = True
        heavens_forge_landing()
    elif choice == 4:
        Player.gameplay = True
        wormwood_planet()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 3-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def acropolis():
    supervisor()
    Player.gameplay = False
    if "Sun Seared Navigator" not in Player.on_board:
        print("\nYou can not find a way to safely land in Acropolis\n")
        input("Press enter go back to Wormwood Planet\n")
        wormwood_planet()
    gameplay_speed('acropolis')
    Player.planets_visited['acropolis'] = True
    typing_effect(get_file(r"storyline/Acropolis/Acropolis"), DeveloperControls.sleep_time)
    choice = number_validation(4)
    if choice == 1:
        loamstone()
    elif choice == 2:
        Player.gameplay = True
        wormwood_planet()
    elif choice == 3:
        Player.gameplay = True
        twilight_isles_landing()
    else:
        logging.debug("this is being executed @acropolis")


def loamstone():
    supervisor()
    if not Player.planets_visited['loamstone']:
        typing_effect(get_file(r"storyline/location_3/loamstone"), DeveloperControls.sleep_time)
        print("""IN FUTURE VISITS TO ACROPOLIS, YOU MAY NOW TRAVEL TO LOAMSTONE! The Reticent Rancher will allow you 
        to gather your own mushrooms, where you may brave the dark and spores to refill your galley. You will trade 
        Food for sanity. This deal is useful if you're sound of mind but low on foodstuffs. Beware: not all mushrooms 
        are equal.
    
            Press enter to continue.
            """)
        Player.inventory['dreamcap'] = 1
        Player.planets_visited['loamstone'] = True
        input('')
    else:
        print("Welcome to Loamstone!")
    print("\nYou may\n[1]pick some mushrooms\n[2]return to acropolis")
    choice = number_validation(3)
    if choice == 1:
        picking_mushrooms()
    if choice == 2:
        acropolis()


def picking_mushrooms():
    Player.gameplay = False
    print("Welcome to the mushroom cave!\n")
    print("Feel free to eat as many mushrooms as as you want"
          " but it is wise to keep your eye on your sanity levels")
    while True:
        supervisor()
        mushroom_picker(r"tables/picking mushrooms.csv")
        print("\nenter [1] to return to Loamstone, press enter to pick more mushrooms.")
        user_choice = input()
        if user_choice == "1":
            loamstone()
            Player.gameplay = True


def mushroom_picker(csv):
    table = pandas.read_csv(csv)
    print(table)
    row_choice = input("Enter the index value of the mushroom you want to pick, or press enter to skip\n")
    if row_choice == "":
        return
    try:
        int(row_choice)
    except ValueError:
        print("Please only enter numbers\n")
        return
    try:
        row = table.iloc[int(row_choice)]
    except IndexError:
        print("Please enter the index number of the mushroom you want to purchase.\n")
    row_dict = row.to_dict()
    print("Purchase " + row["ITEM NAME"] + " for " + str(row["PRICE(SANITY)"]) + " sanity?\n")
    choose = yes_or_no(input("[yes] or [no]\n"))
    if choose != "yes":
        return
    if row["PRICE(SANITY)"] <= Player.stats["sanity"]:
        Player.stats['sanity'] -= int(row["PRICE(SANITY)"])
        if row_dict["RESOURCE"] == 'food':
            Player.stats['food'] += int(row['AMOUNT'])
        else:
            Player.inventory[row_dict["ITEM NAME"]] = 1
        table = table.drop(int(row_choice), axis=0)
        table.to_csv(csv, index=False)
    else:
        print("you do not have the mental fortitude to pick this mushroom")
        time.sleep(2)


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 4-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_4():
    supervisor()
    print("this is task 4")
    input('return to location 4')
    wormwood_planet()


def wormwood_planet():
    supervisor()
    Player.gameplay = False
    typing_effect(get_file(r"storyline/location_4/Wormwood Planet"), DeveloperControls.sleep_time)
    choice = int(input("Enter a [1-3]"))
    if choice == 1:
        task_4()
    elif choice == 2:
        Player.gameplay = True
        location_5()
    elif choice == 3:
        Player.gameplay = True
        acropolis()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 5-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def task_5():
    supervisor()
    print("this is task 5")
    input('return to location 5')
    Player.gameplay = True
    location_5()


def location_5():
    supervisor()
    typing_effect(get_file(r"storyline/location_5/Mars"), DeveloperControls.sleep_time)
    choice = int(input("Enter a [1-3]"))
    if choice == 1:
        task_5()
    elif choice == 2:
        Player.gameplay = True
        location_6()
    elif choice == 3:
        Player.gameplay = True
        wormwood_planet()


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
    Player.gameplay = False
    typing_effect(get_file(r"storyline/location_6/Cobatiania"), DeveloperControls.sleep_time)
    choice = int(input("Enter a [1-3]"))
    if choice == 1:
        task_6()
    elif choice == 2:
        Player.gameplay = True
        location_7()
    elif choice == 3:
        Player.gameplay = True
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
    choice = int(input("Enter a [1-3]"))
    if choice == 1:
        task_7()
    elif choice == 2:
        heavens_forge_landing()
    elif choice == 3:
        location_6()


# -------------------------------------------------------------------------------------------------------------------
twilight_isles_landing()
