import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = None

    while user not in choices:
        user = input("Please, select one from rock, paper or scissors: ")

    if user == computer:
        print(f"Machine: {computer}")
        print(f"Player: {user}")
        print(f"Tie!")

    elif user == 'rock':
        if computer == 'paper':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've lost!")

        if computer == 'scissors':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've won!")

    elif user == 'scissors':
        if computer == 'paper':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've won!")

        if computer == 'rock':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've lost!")

    elif user == 'paper':
        if computer == 'scissors':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've lost!")

        if computer == 'rock':
            print(f"Machine: {computer}")
            print(f"Player: {user}")
            print(f"You've won!")

    play_again = input("Do you want to play again? (yes / no)")

    if play_again != 'yes':
        break
