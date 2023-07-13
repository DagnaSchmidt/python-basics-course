import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

player1_name = input('Enter player 1 name:\n')
player2_name = input('Enter player 2 name:\n')

roll_1 = roll_dice()
roll_2 = roll_dice()

print(player1_name, 'rolled', roll_1)
print(player2_name, 'rolled', roll_2)

if (roll_1 > roll_2):
    print(player1_name, 'won!')
else:
    print(player2_name, 'won!')