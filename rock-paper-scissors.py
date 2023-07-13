import random

choices = ['paper', 'rock', 'scissors']

computer_choice = random.choice(choices)
user_choice = input("Choose rock, paper or scissors\n")

print('Computer choice: ' + computer_choice )

if computer_choice == user_choice:
    print('TIE')
elif computer_choice == 'rock' and user_choice == 'paper':
    print('WIN')
elif computer_choice == 'scissors' and user_choice == 'rock':
    print('WIN')
elif computer_choice == 'paper' and user_choice == 'scissors':
    print('WIN')
else:
    print('LOSE')