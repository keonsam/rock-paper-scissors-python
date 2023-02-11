import random

choices = ["rock", "paper", "scissors"]
while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("What is your choice, {}? ".format(choices)).lower()

    if ((player == choices[0] and computer == choices[2]) or
        (player == choices[1] and computer == choices[0]) or
        (player == choices[2] and computer == choices[1])
    ):
        print("computer {}".format(computer))
        print("player {}".format(player))
        print("You win")
    elif (player == computer):
        print("computer {}".format(computer))
        print("player {}".format(player))
        print("It's a draw")
    else:
        print("computer {}".format(computer))
        print("player {}".format(player))
        print("You lose")
    play_again = input("Do you want to play again, (y/n)?").lower()[0]

    if (play_again == 'n'):
        break

print("Bye!")