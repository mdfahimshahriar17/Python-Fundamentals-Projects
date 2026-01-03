from rock_papper_scissor_ASCII_art import image
import random

result = ""

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)

if user_choice >=3 or user_choice <0:
    print("You type an invalid number!")
else:
    print(f"You chose {image[user_choice]}")
    print(f"Computer chose: {computer_choice} {image[computer_choice]}")


if user_choice == computer_choice:
    result = "Draw"

elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    result = "Win"
else:
    result = "Lose"

if result:
    print(f"You {result}")
