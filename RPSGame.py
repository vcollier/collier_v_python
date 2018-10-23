# import the random package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

def computer_choice_rock():
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print ("It's a Tie!")
        try_again()
    if user_choice == "2":
        print ("You Win! Paper covers Rock!")
        try_again()
    if user_choice == "3":
        print ("I Win and You Lose! Rock crushes Scissors!")
        try_again()
    else:
        print ("Please type in 1, 2, or 3")
        computer_choice_rock()

def computer_choice_paper():
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print ("I Win and You Lose! Paper covers Rock!")
        try_again()
    if user_choice == "2":
        print ("It's a Tie!")
        try_again()
    if user_choice == "3":
        print ("You Win! Scissors cut Paper!")
        try_again()
    else:
        print ("Please type in 1, 2, or 3")
        computer_choice_paper()

def computer_choice_paper():
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == ("1"):
        print ("You Win! Rock crushes Scissors")
        try_again()
    if user_choice == "2":
        print ("I Win! Scissors cut Paper!")
        try_again()
    if user_choice == "3":
        print ("It's a Tie!")
        try_again()
    else:
        print ("Please type in 1, 2, or 3")
        computer_choice_paper()

def try_again():
    choice = input("Would you like to play again? Y/N: ")
    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        rps()
    elif choice == "n" or choice == "N" or choice == "No" or choice == "no":
        print ("Thanks for Playing!")
        quit()
    else:
        print ("Please type Y or N")
        try_again()

# print the choice to the terminal window.
print("computer chooses: ", computer_choice)