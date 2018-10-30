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

# set up our loop
restart = "Yes"

while restart == "Yes":

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
    print("computer chooses: ", computer_choice)

    # scoreboard
    print('You', score1, 'Computer', score2)

    # when lives run out
    if score1 == 0:
        print("Sorry you are out of lives. Better luck next time.")

    elif score2 == 0:
        print("Congrats you win!")

    # when player or computer reaches 0, game ends
    if score1 == 0:
        print("Sorry, you lose.")
        restart = input("Do you want to restart the game? Yes or No\n")

    elif score2 == 0:
        print("You beat the computer!")
        restart = input("Do you want to restart the game? Yes or No\n")
