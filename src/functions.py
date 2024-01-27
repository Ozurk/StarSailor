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
        time.sleep(.01)
        # todo add a parameter called wait time


def dice():
    number = random.randint(1, 6)
    return number


def stats(food, money, sanity):
    print("\n" * 4)
    print("Your Food Level is at :" + str(food) + " %".center(150, "-"))
    print("-" * 175)
    print("You have " + str(money) + "Platinum Disks")
    print("-" * 175)
    print("Your Sanity is at " + str(sanity) + "%")


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


def user_number_validation(user_number):
    while True:
        if user_number.strip().isnumeric():
            return user_number[0]
        else:
            user_number = input("input a single number:\n")


