import random

roll = random.randint(1, 6)

guess = int(input("guess the dice roll\n"))

if guess == roll:
    print("Correct! Dice rolled : " + str(roll))
else:
    print("Wrong! Dice rolled : " + str(roll))