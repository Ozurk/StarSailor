import sys
import time
import re


def get_file(file_path):
    file = open(file_path, "r")
    text = file.read()
    text = text.strip()
    file.close()
    return text


def typing_effect(string, wait_time):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(wait_time)  # this controls the speed of the game


def text_regex(text):
    alphabet_regex = re.compile("[a-zA-Z]+")
    mo = alphabet_regex.findall(text)
    return mo
    # will return a list of strings


def one_or_two():
    user_input = input("\n Enter [1] or [2]\n")
    if user_input == "1":
        return int(user_input)
    elif user_input == "2":
        return int(user_input)
    else:
        print("You must enter 1 or 2")
        one_or_two()


def yes_or_no(yes_or_no_input):
    options = ['yes', 'no']
    while yes_or_no_input.lower().strip() not in options:
        yes_or_no_input = input("Please enter\n[yes]\nor\n[no]")
    if yes_or_no_input == "yes":
        return yes_or_no_input
    if yes_or_no_input == "no":
        return yes_or_no_input

def number_regex(number):
    numberregex = re.compile("d+")
    mo = numberregex.findall(number)
    return mo

print(number_regex("5"))