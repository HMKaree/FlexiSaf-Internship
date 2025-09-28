# Import libraries
import random

def rock_paper_scissors():
    # Define possible choices
    choices = ['rock', 'paper', 'scissors']
    
    # Get the user's choice
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in choices:
            break  # Valid choice, exit the loop
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    # Generate random choice for computer
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Print result and choices
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

# Run the game
rock_paper_scissors()
