# import the random package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

score1 = 5
score2 = 5

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0, 2)]


# def win or lose function
def winorlose(status):
    print("Called win or lose funcation")
    print("*********************************************")
    print("You", status, " ! Would you like to play again?")
    choice = input("Y / N: ")

    # reset the lives
    if choice == "Y" or choice == "y":
        # change global variables
        global score1
        global score2
        global player
        global computer

        score1 = 5
        score2 = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n":
        print("You chose to quit!")
        print("**********************************************")
        exit()


# set up our loop
restart = "Yes"

while player is False:
    print("==============================================")
    print("Player lives:", score1, "/5")
    print("Computer lives:", score2, "/5")
    print("==============================================")

    # set player to True by making a selection
    print("Choose you weapon!")
    player = input("Rock, Paper, Scissors?\n")

    print(player, "\n")
    # check for a tie = choice are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. crap!!
            print("You lose! Paper covers Rock")
            score1 = score1 - 1
        else:
            # we win! such winning
            print("You win!", player, "smashes", computer_choice)
            score2 = score2 - 1

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player)
            score1 = score1 - 1
        else:
            print("You win!", player, "covers", computer_choice)
            score2 = score2 - 1

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player)
            score1 = score1 - 1
        else:
            print("You win!", player, "cut", computer_choice)
            score2 = score2 - 1

    elif player == "quit":
        exit()
    else:
        print("Check your spelling... that's not a valid choice\n")

        # show computers choice in the terminal window
    print("computer chose: ", computer_choice)


    # check for win or lose
    if score1 is 0:
        winorlose("lose")

    if score2 is 0:
        winorlose("win")

    player = False
    computer = choices[randint(0, 2)]
