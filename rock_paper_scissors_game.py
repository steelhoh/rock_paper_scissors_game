import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_choice = ""
computer_input = ""
player_won = False

#Player actions

player_input = input("Make your choice. Press 'r' for 'Rock', 'p' for 'Paper' or 's' for 'Scissors': ")

if player_input.lower() == 'r':
    player_choice = rock

elif player_input.lower() == 'p':
    player_choice = paper

elif player_input.lower() == 's':
    player_choice = scissors

else:
    print("Invalid Move! Try again...")
    exit()

# Coputer actions
computer_input = random.randint(1, 3)
if computer_input == 1:
    computer_choice = rock

elif computer_input == 2:
    computer_choice = paper

elif computer_input == 3:
    computer_choice = scissors

# Who is the winner?

if computer_choice == player_choice:
    print(colored("The Game is Draw", 'yellow'))
    print(f"You both chose {player_choice}")

elif computer_choice == rock and player_choice == paper:
    player_won = True

elif computer_choice == paper and player_choice == scissors:
    player_won = True

elif computer_choice == scissors and player_choice == rock:
    player_won = True

else:
    print(f'The computer won, as {computer_choice} beats {player_choice}')

if player_won:
    print(f'Congratulations YOU are the winner, as {player_choice} beats {computer_choice}!')
