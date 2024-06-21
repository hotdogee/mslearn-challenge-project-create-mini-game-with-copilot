# the winner of the game is determined by three simple rules:

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.

# where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Run the minigame on the console with the python app.py command.
# At the prompt, type one of the game options: rock, paper, or scissors.
# The minigame should inform the player whether the player won, lost, or tied with the opponent.
# Choose to continue playing.
# At the prompt, type screen.
# The minigame should inform the player if the option entered by the player is invalid.
# Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.
# Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.

import random
import sys
import os
import time

def play_game():
    player_score = 0
    rounds = 0
    print("Welcome to the Rock, Paper, Scissors game!")
    while True:
        player_choice = input("Choose rock, paper, or scissors: ")
        player_choice = player_choice.lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue
        print(f"Computer chose {computer_choice}.")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("You lose!")
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("You lose!")
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose!")
            else:
                print("You win!")
                player_score += 1
        rounds += 1
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break
    print(f"Game over! Your score was {player_score} in {rounds} rounds.")

if __name__ == "__main__":
    play_game()


