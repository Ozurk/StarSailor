# this is the functions file for project StarSailor
# todo make a function for getting a file and returning the text from it
# todo make a function that reads the text
# todo make a random number dice thing

import sys
import time
import random
import re


def get_file(file_path):
    file = open(file_path, "r")
    text = file.read()
    text = text.strip()
    file.close()
    return text


def typing_effect(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.00)  # this controls the speed of the game
        # todo add a parameter called wait time


def user_stats(food, money, sanity):
    print("\n" * 4)
    print("-" * 110)
    print("Your Food Level is at " + str(food) + "%")
    print("-" * 110)
    print("You have " + str(money) + " Platinum Disks")
    print("-" * 110)
    print("Your Sanity is at " + str(sanity) + "%")
    print("-" * 110)
    # user_stats(stats["food"], stats["money"], stats["sanity"])
    # input("press enter to continue...".center(110, " "))
    # os.system("cls")


def text_regex(text):
    alphabet_regex = re.compile("[a-zA-Z]+")
    mo = alphabet_regex.findall(text)
    return mo
    # will return a list of strings


def intro_screen():
    # this is the fancy little intro screen
    typing_effect("-" * 110)
    print()
    typing_effect("-" * 110)
    print()
    typing_effect("-" * 110)
    typing_effect("""
                 #####                       #####                                
                #     # #####   ##   #####  #     #   ##   # #       ####  #####  
                #         #    #  #  #    # #        #  #  # #      #    # #    # 
                 #####    #   #    # #    #  #####  #    # # #      #    # #    # 
                      #   #   ###### #####        # ###### # #      #    # #####  
                #     #   #   #    # #   #  #     # #    # # #      #    # #   #  
                 #####    #   #    # #    #  #####  #    # # ######  ####  #    # """.center(150, " "))
    print("\n")
    typing_effect("-" * 110)
    print()
    typing_effect("-" * 110)
    print()
    typing_effect("-" * 110)
    time.sleep(.75)
    print()
    # input("Press Enter to Continue...".center(110, " "))
    # todo un-comment this ^


def one_or_two():
    user_input = input("Choose \n[1] \nor \n[2]\n")
    if user_input == "1":
        return int(user_input)
    elif user_input == "2":
        return int(user_input)
    else:
        print("You must choose between 1 or 2")
        one_or_two()


def storyline_splitter(integer, option_1, option_2):
    if integer == 1:
        option_1()
    elif integer == 2:
        option_2()
