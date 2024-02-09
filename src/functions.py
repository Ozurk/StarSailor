import sys
import time
import re
import shutil
terminal_width = shutil.get_terminal_size().columns
def intro_screen():
    # this is the fancy little intro screen
    typing_effect("-" * 115, .005)
    print()
    typing_effect("-" * terminal_width, .005)
    print()
    typing_effect("-" * terminal_width, .005)
    typing_effect("""  
             #####  #######    #    ######   #####     #    ### #       ####### ######  
            #     #    #      # #   #     # #     #   # #    #  #       #     # #     # 
            #          #     #   #  #     # #        #   #   #  #       #     # #     # 
             #####     #    #     # ######   #####  #     #  #  #       #     # ######  
                  #    #    ####### #   #         # #######  #  #       #     # #   #   
            #     #    #    #     # #    #  #     # #     #  #  #       #     # #    #  
             #####     #    #     # #     #  #####  #     # ### ####### ####### #     # """, .005)
    print("\n")
    typing_effect("-" * terminal_width, .005)
    print()
    typing_effect("-" * terminal_width, .005)
    print()
    typing_effect("-" * terminal_width, .005)
    time.sleep(.75)
    print("\n" * 8)
    input("Press Enter to Continue...".center(terminal_width, " ") + "\n")
    print("\n")


def get_file(file_path):
    file = open(file_path, "r", encoding="utf-8")
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
    numberregex = re.compile(r"\d+")
    mo = numberregex.findall(number)
    return int(mo[0])


def spinner(load_time):
    for iteration in range(load_time * 5):
        sys.stdout.write('\rwaiting |')
        time.sleep(.05)
        sys.stdout.write('\rwaiting /')
        time.sleep(.05)
        sys.stdout.write('\rwaiting -')
        time.sleep(.05)
        sys.stdout.write('\rwaiting \\')
        time.sleep(.05)
    sys.stdout.write('\r')


def one_through_3():
    user_input = input("\n Enter \n[1]\n[2]\n[3]\n")
    if user_input.strip() == "1":
        return int(user_input)
    elif user_input.strip() == "2":
        return int(user_input)
    elif user_input.strip() == "3":
        return int(user_input)
    else:
        input("You must enter 1, 2, or 3\n\npress enter to retry")
        one_through_3()
