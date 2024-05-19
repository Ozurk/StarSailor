import logging
import random
import time
import pandas
import tkinter as tk
from functions import *
from random import randint
import pyautogui
from reset_tables import reset_tables_v2
import sys

# ---------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------Settings and Controls-------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
terminal_width = shutil.get_terminal_size().columns


class DeveloperControls:
    sleep_time = 0.000  # delay between letters in typing effect. This gets assigned in the gameplay speed function
    iteration = 1  # this is just for the slot machine module

    def __init__(self):
        pass


class Player:
    stats = {"money": 10000, "sanity": 50, "food": 100.00}
    inventory = {"rope": 40}
    gameplay = False
    planets_visited = {"intro": False, "heavens forge": False, "twilight isles": False, "acropolis": False,
                       "loamstone": False,
                       "ch'tak": False, "mars": False, "cobaltiania": False, "B-IRS": False, "talashandra": False,
                       "sun seared navigator": False, "grifter's drift": False}
    on_board = {}

    critical_events = {"talashandra": False, "talashandra 2": False, "talashandra 3": False, "gas giants": False,
                       "rancher": False}

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
        elif Player.stats['sanity'] >= 100:
            Player.stats['sanity'] = 100
        if Player.stats['money'] <= 0:
            beg()
        if randint(1, 15) == 1:
            random_event()
    user_stats()
    debug = input("\n")
    planet_list = list(Player.planets_visited.keys())
    event_list = list(Player.critical_events.keys())

    index = 0
    if debug == "debug":
        DeveloperControls.sleep_time = 0.0
        for number in planet_list:
            planet = planet_list[index]
            Player.planets_visited[planet] = True
            print(number, index)
            index += 1
        index = 0
        for number in event_list:
            event = event_list[index]
            Player.critical_events[event] = True
            index += 1
        print(Player.planets_visited)

    if debug == "play":
        index = 0
        for number in planet_list:
            planet = planet_list[index]
            Player.planets_visited[planet] = False
            index += 1
        index = 0
        for number in event_list:
            event = event_list[index]
            Player.critical_events[event] = False
            index += 1
        print(Player.planets_visited, Player.critical_events)
    if debug == "reset":
        reset_tables_v2()
        input("The marketplaces have been reset")
    if debug == "Acropolis":
        if Player.planets_visited["acropolis"]:
            acropolis()


def gameplay_speed(location):
    if Player.planets_visited[location]:
        DeveloperControls.sleep_time = .00
    else:
        DeveloperControls.sleep_time = .0001


# TODO make the portal to get to acropolis. ie, enter acroplis and go to acropolis from anywhere. like the dubug

# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------------Consequences and Menu----------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def insane():
    print("you lost your mind")
    input("press enter to continue...\n")
    # todo make a better insanity screen
    while True:
        pyautogui.moveRel(80, -80, .03)
        print("all work and no play makes Jack a dull boy.")


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
        Player.stats['sanity'] *= .99
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
    print("You have been selected for inter-galactic jury duty by the highest power in deep space...\nDespite all "
          "efforts, you can not wiggle out of this one...\nYou lose a little bit of your mind...")
    print('\n')
    print("-" * terminal_width)
    input('Press Enter to Continue\n')
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


def item_purchaser(csv, row_choice):
    if row_choice == "":
        return
    try:
        int(row_choice)
    except ValueError:
        print("Please only enter numbers\n")
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


def item_seller(csv, row_choice):
    if row_choice == "":
        return
    try:
        int(row_choice)
    except ValueError:
        input("Please only enter numbers\n")
        return
    table = pandas.read_csv(csv)
    try:
        sale_item_row = table.iloc[int(row_choice)]
    except IndexError:
        print("Please enter the index number of the item you want to sell.\n")
        time.sleep(2)
        return
    player_inventory = list(Player.inventory.keys())
    sale_item_as_dict = sale_item_row.to_dict()
    if sale_item_as_dict["ITEM"] not in player_inventory:
        print("You do not have the item you want to sell, please try again with the item you want in your inventory\n")
        time.sleep(2)
        return
    quantity = input("Enter the amount you want to sell.\n")
    try:
        int(quantity)
    except ValueError:
        input('Please enter an integer.\n')
        return
    for sales in range(int(quantity)):
        item_name = sale_item_as_dict["ITEM"]
        Player.inventory[item_name] -= 1
        if Player.inventory[item_name] == 0:
            Player.inventory.pop(item_name)
        Player.stats["money"] += int(sale_item_as_dict["VALUE"])


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
    tunnel()


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
    print("do you want purchase [1] or sell items [2] at the market?\n")
    user_choice = number_validation(3)
    if user_choice == 2:
        print(pandas.read_csv(r"tables\sales\hforge.csv"))
        user_input_sales = input("\nEnter the ID of the item you would like to purchase, or press enter to leave...\n")
        item_seller("tables\\sales\\hforge.csv", user_input_sales)
    if user_choice == 1:
        market = pandas.read_csv(r"tables/heaven's forge market.csv")
        print(market)
        user_input = input("\nEnter the ID of the item you would like to sell, or press enter to leave...\n")
        item_purchaser(r"tables/heaven's forge market.csv", user_input.strip())
    heavens_forge_landing()


def overclocked_lightwelder():
    supervisor()
    if 'starpaint' in Player.inventory.keys():
        typing_effect(get_file(r"storyline/Heaven's Forge/Lightwelder[starpaint]"), DeveloperControls.sleep_time)
        input("\nPress enter to continue\n")
        Player.inventory['hardlight'] = 1
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
    print("\n[1] Approach an Overclocked Welding Robot\n[2] Go to B-IRS\n[3] Go to Twilight Isles\n[4] Visit the "
          "marketplace")
    choice = number_validation(5)
    if choice == 1:
        overclocked_lightwelder()
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


def turtles():
    Player.inventory["Map"] = 1
    Player.critical_events["turtles"] = True


def sun_seared_navigator():
    supervisor()
    try:
        if Player.on_board["Sun Seared Navigator"]:
            input("\n The navigator is in your ship..\n")
            twilight_isles_landing()
    except KeyError:
        typing_effect(get_file(r"storyline/Twilight Isles/roasted navigator"), DeveloperControls.sleep_time)
        print("\n[1] INVITE THE SUN SEARED NAVIGATOR ABOARD\n[2] Leave.")
        choice = number_validation(3)
        if choice == 1:
            Player.on_board["Sun Seared Navigator"] = True
            twilight_isles_landing()
        elif choice == 2:
            twilight_isles_landing()


def twilight_isles_market():
    supervisor()
    print("Welcome to to Twilight Isles Floating Market".center(terminal_width))
    print("\n")
    market = pandas.read_csv("tables/twilight isles market.csv")
    print("Would you like to purchase [1] or sell [2] at the market?\n")
    user_input = number_validation(3)
    if user_input == 1:
        print(market)
        user_input = input("Please enter the index number of the item you would like to purchase\n")
        item_purchaser(r"tables/twilight isles market.csv", user_input.strip())
    elif user_input == 2:
        print(pandas.read_csv("tables/sales/twilight.csv"))
        user_sales_input = input("Enter the ID of the item you would like to sell, or press enter to leave\n")
        item_seller("tables/sales/twilight.csv", user_sales_input.strip())
    twilight_isles_landing()


def twilight_isles_landing():
    supervisor()
    Player.gameplay = False
    gameplay_speed("twilight isles")
    Player.planets_visited["twilight isles"] = True
    typing_effect(get_file(r"storyline/Twilight Isles/Twilight Isles landing"), DeveloperControls.sleep_time)
    print("\n[1] Approach a Bandaged Navigator\n[2] Travel to Ch'Tak\n[3] Return to Heaven's Forge\n[4]"
          " Visit the Market Place\n[5] Attempt to get to Acropolis")
    choice = number_validation(6)
    if choice == 1:
        if Player.planets_visited["loamstone"]:
            input("You already took the navigator home")
            twilight_isles_landing()
        sun_seared_navigator()
    elif choice == 4:
        twilight_isles_market()
    elif choice == 3:
        Player.gameplay = True
        heavens_forge_landing()
    elif choice == 2:
        Player.gameplay = True
        chtak_landing()
    elif choice == 5:
        Player.gameplay = True
        acropolis()
    elif choice == 6:
        if not Player.critical_events['talashandra 3']:
            input("please enter a number in the range")
            twilight_isles_landing()
        turtles()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 3-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def acropolis_market():
    supervisor()
    print("do you want purchase [1] or sell [2] at the market?\n")
    user_choice = number_validation(3)
    if user_choice == 2:
        print(pandas.read_csv(r"tables\sales\acropolis.csv"))
        user_input_sales = input("\nEnter the ID of the item you would like to purchase, or press enter to leave...\n")
        item_seller("tables\\sales\\acropolis.csv", user_input_sales)
    if user_choice == 1:
        market = pandas.read_csv(r"tables/Acropolis market.csv")
        print(market)
        user_input = input("\nEnter the ID of the item you would like to sell, or press enter to leave...\n")
        item_purchaser(r"tables/Acropolis market.csv", user_input.strip())
    acropolis()


def acropolis():
    supervisor()
    Player.gameplay = False
    if not Player.planets_visited["acropolis"]:
        if "Sun Seared Navigator" not in Player.on_board:
            input("You can not find a way to safely land on Acropolis. \nPress enter to land on Twilight Isles\n")
            twilight_isles_landing()

    gameplay_speed('acropolis')
    Player.planets_visited['acropolis'] = True
    typing_effect(get_file(r"storyline/Acropolis/Acropolis"), DeveloperControls.sleep_time)
    print("\n[1] Continue to Loamstone\n[2] Travel to Ch'Tak\n[3] Return to Twilight Isles\n[4] Visit the Marketplace")
    choice = number_validation(5)
    if choice == 1:
        loamstone()
    elif choice == 2:
        Player.gameplay = True
        chtak_landing()
    elif choice == 3:
        Player.gameplay = True
        twilight_isles_landing()
    elif choice == 4:
        acropolis_market()


def loamstone():
    supervisor()
    try:
        if Player.on_board["Sun Seared Navigator"]:
            Player.on_board.pop("Sun Seared Navigator")
    except KeyError:
        pass

    if not Player.planets_visited['loamstone']:
        typing_effect(get_file(r"storyline/Acropolis/loamstone"), DeveloperControls.sleep_time)
        Player.inventory['dreamcap'] = 1
        Player.planets_visited['loamstone'] = True
        Player.critical_events['rancher'] = True

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


def talashandra():
    if not Player.critical_events["talashandra"]:
        try:
            if not Player.inventory["dreamcap"]:
                chtak_landing()
        except KeyError:
            pass
        typing_effect("\nYOUR DREAMCAP HAS CAUGHT SOMEONES' ATTENTION\n", DeveloperControls.sleep_time)
        typing_effect("A morchella on eight vined tentacles abruptly stops as it scuttles by you, veering back around."
                      "Its honeycombed cap puckers tenuously at something in the air you can't quite perceive, "
                      "til it points aggressively at your pack. It continues impatiently until you produce the "
                      "Dreamcap.",
                      DeveloperControls.sleep_time)
        input("\n")
        os.system("cls")
        typing_effect("A shudder runs down its body, and it dashes a short distance away before turning back and "
                      "beckons you to follow. It leads you down, to the foot of the fort, among a lake of frozen mud. "
                      "On its surface lay a massive lotus flower, as large as your ship. You both cross the makeshift "
                      "docks reaching out to it and carefully climb up into its center. The morchella takes a sitting "
                      "position and holds your hands in two of its tentacles. The remaining limbs gesticulate in a "
                      "ceremonial quality before one of them drops the Dreamcap into one of the pits on its head.",
                      DeveloperControls.sleep_time)
        input("\n")
        os.system("cls")
        typing_effect("The creature expands as if taking a deep breath, the breathes out a thick cloud of starry "
                      "spores that immediately succumb you to slumber... Your eyes flutter open, and you find "
                      "yourself in a golden court. There is a certain warmth and cheer in the air here. The sound of "
                      "merriment and the smell of roses brings to your attention the fact that you are not alone. A "
                      "plethora of alien characters, each more exotic in shape and size than the last, "
                      "laugh and drink around you. But you only catch vague glimpses of them from the corner of your "
                      "eye, for your gaze is fixed upon the throne in the center of the room, and the figure perched "
                      "upon it.", DeveloperControls.sleep_time)
        input('\n')
        os.system("cls")
        typing_effect("An amber mushroom man lounges, eight feet tall even in a sitting position, as thick as a tree "
                      "trunk, draped in finery of deepest sapphire and cradling a blade of shimmering Starglass "
                      "between his rooted arms and legs. Sharp, fierce periwinkle pupils betray droopy eyelids "
                      "beneath the brim  his golden cap. The camaraderie of the court drowns out as your mind fills "
                      "with a voice as fierce as sunlight and rich as honey. ", DeveloperControls.sleep_time)
        input('\n')
        typing_effect("I am Emperor Talashandra, Speaker of Posterity. What a queer creature you are, to find your "
                      "way here. I sense... this is a dream, no? Curious creature indeed. It seems we are speaking "
                      "across a gap spanning thousands of years. I suppose one of my spores carried out its way "
                      "through the ages and came to be in your possession, affording us this conversation. What a "
                      "novelty! Tell me little creature, what do you know of... actually, perhaps its best I not pry "
                      "into the future. There may be danger in that knowledge. But there is no danger in sharing my "
                      "knowledge with you. And so much has been lost! I sense no capacity for my language in your "
                      "thoughts, allow me to instruct you.", DeveloperControls.sleep_time)
        input('\n')
        os.system("cls")
        typing_effect("'The foundation of all interaction is communication. In your travels you are bound to find "
                      "many that do not share your native tongue. Yet there is a older tongue that precedes the "
                      "flesh. Here are the first word.'Emperor Talashandra's words dissolve into something akin to a "
                      "guttural throat chant, deeper than any voice you've ever heard. It threatens to dispel the "
                      "dream and send you back to your time until finally, your brain buzzes with a newfound "
                      "awakening of forgotten primordial understanding. 'There. May your words never be barred by "
                      "ignorance again. Take this boon and go forward as a diplomat for posterity. I feel this dream "
                      "fading, and soon you will waken. Search for my gifts in the future, I have more words for you. "
                      "Next I will show you to how to speak with the very stone...",
                      DeveloperControls.sleep_time)
        input('\n')
        os.system("cls")
        typing_effect("You are already struggling to remember his words as you awake, but you feel a new power "
                      "dwelling inside you. The morchella has continued holding you up while you entered the trance, "
                      "and wriggles with delight as you come to your senses. The buzzing starts at the edge of your "
                      "consciousness again as its voice echos through your thoughts. 'Oh, hello? Excellent, "
                      "friend! I am this tribe's shaman. To bestow such a gift upon us as that Dreamcap is sacred, "
                      "and we recognize you as family now. I am happy to answer any further questions back in the "
                      "village, but shall we return for now? You're bound to get hypothermia out here if we stay any "
                      "longer.'\nPress enter to return to the Wilderfolk village.", DeveloperControls.sleep_time)
        input("\n")
        Player.critical_events["talashandra"] = True


def task_4():
    supervisor()

    chtak_landing()


def chtak_market():
    supervisor()
    print("do you want purchase [1] or sell [2] at the market?\n")
    user_choice = number_validation(3)
    if user_choice == 2:
        print(pandas.read_csv(r"tables\sales\chtak.csv"))
        user_input_sales = input("\nEnter the ID of the item you would like to purchase, or press enter to leave...\n")
        item_seller("tables\\sales\\chtak.csv", user_input_sales)
    if user_choice == 1:
        market = pandas.read_csv(r"tables\chtak market.csv")
        print(market)
        user_input = input("\nEnter the ID of the item you would like to sell, or press enter to leave...\n")
        item_purchaser(r"tables/chtak market.csv", user_input.strip())
    chtak_landing()


def chtak_landing():
    supervisor()
    Player.gameplay = False
    Player.planets_visited["ch'tak"] = True
    if not Player.critical_events['talashandra']:
        if Player.critical_events["rancher"]:
            talashandra()
    elif not Player.critical_events['talashandra']:
        typing_effect(get_file("storyline\\Ch'Tak\\Ch'Tak"), DeveloperControls.sleep_time)
    else:
        print("Welcome back to Ch'tak!\nThe Wilderfolk greet you with open arms\n")
    print("\nWelcome to Ch'tak!\n[1]talk the shaman\n[2]travel to Valdstafar\n[3]Travel to Twilight Isles\n[4]visit the market ")
    choice = number_validation(5)
    if choice == 1:
        task_4()
    elif choice == 2:
        Player.gameplay = True
        valdstafar_landing()
    elif choice == 3:
        Player.gameplay = True
        twilight_isles_landing()
    elif choice == 4:
        if not Player.critical_events["talashandra"]:
            input("You can not communicate with the Wilderfolk, they will not even acknowledge your existence\n")
            chtak_landing()
        chtak_market()
    elif choice == 5:
        if not Player.critical_events['talashandra']:
            input("No matter how hard you try, you can not get the Wilderfolk's attention.\n")
            chtak_landing()
        pass


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 5-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

def unnamed_event_1():
    Player.critical_events['talashandra 2'] = True


def unnamed_event_2():
    Player.critical_events['gas giants'] = True


def valdstafar_market():
    supervisor()
    print("do you want purchase [1] or sell [2] at the market?\n")
    user_choice = number_validation(3)
    if user_choice == 2:
        print(pandas.read_csv(r"tables\sales\valdstafar.csv"))
        user_input_sales = input("\nEnter the ID of the item you would like to purchase, or press enter to leave...\n")
        item_seller("tables\\sales\\valdstafar.csv", user_input_sales)
    if user_choice == 1:
        market = pandas.read_csv(r"tables\valdstafar market.csv")
        print(market)
        user_input = input("\nEnter the ID of the item you would like to sell, or press enter to leave...\n")
        item_purchaser(r"tables\valdstafar market.csv", user_input.strip())
    valdstafar_landing()


def slot_machine():
    Player.gameplay = False
    os.system("cls")
    print("[2] Return to Casino Lobby")
    if Player.stats['money'] < 50:
        input("You do not have enough money to play the slot machine\nPress enter to continue.\n")
    Player.stats['food'] += 3
    print("-" * terminal_width)
    print("press enter for a chance to win big using the slot machine!\n")
    print("-" * terminal_width)
    print("Only 100 PD per round!")
    print("-" * terminal_width)
    Player.stats['money'] -= 100
    print("-" * terminal_width)
    print("If you get three of a kind, you win 1000 PD")
    print("-" * terminal_width)
    print("If all three numbers multiply to equal 234, you win 10000 PD")
    print("-" * terminal_width)
    number_1 = random.randint(1, 9)
    number_2 = random.randint(1, 9)
    number_3 = random.randint(1, 9)
    number_4 = random.randint(1, 9)
    number_spinner()
    print("|" + str(number_1) + "|")
    number_spinner()
    print("|" + str(number_2) + "|")
    number_spinner()
    print("|" + str(number_3) + "|")
    number_spinner()
    print("|" + str(number_4) + "|")
    if number_1 == number_2 == number_3:
        input("Congratulations! You won 1000 PD\nPress enter to continue.\n")
        Player.stats["money"] += 1000
    elif number_2 == number_3 == number_4:
        input("Congratulations! You won 1000 PD\nPress enter to continue.\n")
        Player.stats["money"] += 1000
    elif number_1 == number_3 == number_4:
        input("Congratulations! You won 1000 PD\nPress enter to continue.\n")
        Player.stats["money"] += 1000
    elif number_1 == number_2 == number_4:
        input("Congratulations! You won 1000 PD\nPress enter to continue.\n")
    elif number_1 * number_2 * number_3 * number_4 == 234:
        print("congratulations! You hit the jackpot of 100000 PD\n")
        Player.stats['money'] += 100000
    else:
        print("You did not win anything. Please Try again\n")
    user_choice = input("")
    if user_choice == "2":
        casino()
    slot_machine()


def casino():
    root = tk.Tk()
    root.title("Game Menu")
    slot_machine_button = tk.Button(root, text="Slot Machine", command=slot_machine)
    slot_machine_button.pack(pady=10)
    poker_button = tk.Button(root, text="Poker", command=poker)
    poker_button.pack(pady=10)
    return_button = tk.Button(root, text="Leave", command=lambda: return_to_landing(root))
    return_button.pack(pady=10)
    root.mainloop()


def return_to_landing(root):
    root.destroy()
    valdstafar_landing()



def poker_setup():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    player_hand = []
    cpu1_hand = []
    cpu2_hand = []
    cpu3_hand = []
    cpu_list = [cpu1_hand, cpu2_hand, cpu3_hand]
    community_cards = []
    round_counter = 0

    for suite in suites:
        for cards in values:
            deck.append(cards + ": " + suite)

    for cards in range(2):
        cards_in_deck = len(deck) - 1
        random_card = random.randint(1, cards_in_deck)
        player_hand.append(deck[random_card])
        deck.pop(random_card)

    for cards in range(3):
        cards_in_deck = len(deck) - 1
        random_card = random.randint(1, cards_in_deck)
        community_cards.append(deck[random_card])
        deck.pop(random_card)

    for cpus in cpu_list:
        iteration = 0
        for cards in range(2):
            cards_in_deck = len(deck) - 1
            random_card = random.randint(1, cards_in_deck)
            cpus.append(deck[random_card])
            deck.pop(random_card)
    return deck, player_hand, cpu_list, community_cards


def poker():
    deck, player_hand, cpu_list, community_cards = poker_setup()
    print("Welcome to the poker table.\n")
    print(("Here are your cards: [" + player_hand[0] + "][" + player_hand[1] + "]").center(terminal_width))
    print("Pay your blind?  [100 PD]\n[1] yes [2] No")
    user_choice = number_validation(3)
    if user_choice == 2:
        casino()
        return
    if Player.stats["money"] < 100:
        input("you do not have enough money to play.\n press enter to leave")
        valdstafar_landing()
        return
    Player.stats['money'] -= 100
    print(("These are the community cards: [" + community_cards[0] + "][" + community_cards[1] + "][" +
           community_cards[2] + "]").center(terminal_width))


def grifters_drift():
    supervisor()
    input("\nPress Enter to proceed.\n")
    casino()
    Player.gameplay = True
    Player.planets_visited["grifter's drift"] = True
    casino()


def valdstafar_landing():
    supervisor()
    typing_effect(get_file(r"storyline/Valdstafar/Valdstafar"), DeveloperControls.sleep_time)
    print("\n[1] Go to Grifter's Drift\n[2] Go to Titania\n[3] Go to Ch'Tak\n[4] Visit the Market")
    choice = number_validation(5)
    if choice == 1:
        grifters_drift()
    elif choice == 2:
        Player.gameplay = True
        titiana_landing()
    elif choice == 3:
        Player.gameplay = True
        chtak_landing()
    elif choice == 4:
        valdstafar_market()
    elif choice == 5:
        if not Player.critical_events['talashandra']:
            input('You can not do that now\n')
            titiana_landing()
        unnamed_event_1()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 6-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


def unnamed_event_3():
    Player.critical_events['talashandra 3'] = True


def titania_market():
    supervisor()
    print("do you want purchase [1] or sell [2] at the market?\n")
    user_choice = number_validation(3)
    if user_choice == 2:
        print(pandas.read_csv(r"tables\sales\titania.csv"))
        user_input_sales = input("\nEnter the ID of the item you would like to purchase, or press enter to leave...\n")
        item_seller("tables\\sales\\titania.csv", user_input_sales)
    if user_choice == 1:
        market = pandas.read_csv(r"tables/titania market.csv")
        print(market)
        user_input = input("\nEnter the ID of the item you would like to sell, or press enter to leave...\n")
        item_purchaser(r"tables/titania market.csv", user_input.strip())
    titiana_landing()


def task_6():
    supervisor()
    print(get_file("storyline/Titania\\Dr. Chabani"))
    input('return to location 5')
    titiana_landing()


def titiana_landing():
    supervisor()
    Player.gameplay = False
    typing_effect(get_file(r"storyline/Titania/Titiana"), DeveloperControls.sleep_time)
    print("\n[1] \n[2] Go to the B-IRS\n[3] Go to Valdstafar\n[4] Visit the market")
    choice = number_validation(5)
    if choice == 1:
        task_6()
    elif choice == 2:
        Player.gameplay = True
        location_7()
    elif choice == 3:
        Player.gameplay = True
        valdstafar_landing()
    elif choice == 4:
        titania_market()
    elif choice == 5:
        if not Player.critical_events['talashandra 2']:
            input("you can not do that now.\n")
        unnamed_event_3()


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------location 6-----------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

def location_7_market():
    pass


def task_7():
    supervisor()
    print("this is task 7")
    input('return to location 7')
    location_7()


def location_7():
    supervisor()
    typing_effect(get_file(r"storyline/B-IRS/B-IRS"), DeveloperControls.sleep_time)
    choice = number_validation(5)

    if choice == 1:
        task_7()
    elif choice == 2:
        heavens_forge_landing()
    elif choice == 3:
        titiana_landing()
    elif choice == 4:
        location_7_market()


# -------------------------------------------------------------------------------------------------------------------


valdstafar_landing()
