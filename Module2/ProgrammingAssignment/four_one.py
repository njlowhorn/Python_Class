# Python V 3.9.0

import random

secret = random.randint(1, 10)

guess = int(input("Choose a number between 1 and 10: "))

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
