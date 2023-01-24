import random
import math

lower = int(input('Enter lower number: '))
upper = int(input('Enter upper number: '))

x = random.randint(lower, upper)
print("You have only" ,
      round(math.log(upper-lower+1,2)),
      "chances to guess the integer")

count= 0

while count< math.log(upper-lower+1, 2):
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congo, you did it in ", count, "chances")
        break

    elif x < guess:
         print("You guessed to high!!")
    elif x > guess:
         print("You have guessed to low!!")

    if count > math.log(upper-lower+1,2):
        print(" The number is %d" %x)
        print("Better luck next time!")




