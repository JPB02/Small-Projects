from random import choice

play_choices = ["Rock", "Paper", "Scissors"]

print("Make your move!")
play = input()
computer_play = choice(play_choices)
if play == computer_play:
    print("Computer plays:",computer_play)
    print("DRAW")
else:
    if (play == "Rock") and (computer_play == "Paper"):
        print("Computer plays:",computer_play)
        print("YOU LOST!")
    elif (play == "Rock") and (computer_play == "Scissors"):
        print("Computer plays:",computer_play)
        print("YOU WON!")
    elif (play == "Paper") and (computer_play == "Scissors"):
        print("Computer plays:",computer_play)
        print("YOU LOST!")
    elif (play == "Paper") and (computer_play == "Rock"):
        print("Computer plays:",computer_play)
        print("YOU WON!")
    elif (play == "Scissors") and (computer_play == "Rock"):
        print("Computer plays:",computer_play)
        print("YOU LOST!")
    else:
        print("Computer plays:",computer_play)
        print("YOU WON!")
