# Guess the number

import random
n = random.randrange(1,20)
# Print (n)
guess = -1
while n!= guess:
    guess = int(input("Enter any number: "))
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high!")
    else:
      break
print("you guessed it right!!")