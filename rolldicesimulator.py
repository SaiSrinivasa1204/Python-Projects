import random

again = True

while again:
    print(random.randint(1, 6))
    roll_again = input("Do you want to roll the dice again? (y/n):")
    if roll_again.lower() == "y":
        continue
    else:
        input("thanks for playing!! Play again")
          break