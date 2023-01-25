import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('enter a choice(rock, paper, scissors):')

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!!")
    elif player == "rock" and computer == "scissors":
        print('You Win!')
    elif player == "scissors" and computer == "rock":
        print('You Win!')
    elif player == "paper" and computer == "rock":
        print('You Win!')
    else:
        print("You lose!!")

    if not input("play again? (y/n):").lower() == "y":
        running = False
        print("Thanks for playing!!!")


