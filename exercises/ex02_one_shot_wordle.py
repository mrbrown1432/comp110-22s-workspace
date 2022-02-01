"""EX02 - One Shot Wordle"""

__author__ = "73081331"

Secret = "python"

user_name: str = input("What is your 6-letter guess? ")

while len(user_name) != 6:
    while len(user_name) < 6: 
        if len(user_name) < 6:
            user_name: str = input("That was not 6 letters! Try again: ")
    while len(user_name) > 6:
        if len(user_name) > 6:
            user_name: str = input("That was not 6 letters! Try again: ")

while len(user_name) == 6:
    if (user_name) == Secret:
        print("Woo! You got it!") 
        exit()
    else:
        print("Not quite. Play again soon!") 
        exit()