import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or quit): ").lower()
        if user_choice in ["rock", "paper", "scissors", "quit"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, scissors, or quit.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def play_game():
    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            break

        computer_choice = get_computer_choice()

        if user_choice == computer_choice:
            print(f"Computer chose {computer_choice}. It's a draw!")
            draws += 1
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print(f"Computer chose {computer_choice}. You win this round!")
            user_score += 1
        else:
            print(f"Computer chose {computer_choice}. Computer wins this round!")
            computer_score += 1

    print("Game Over")
    print(f"You won {user_score} rounds.")
    print(f"The computer won {computer_score} rounds.")
    print(f"There were {draws} draws.")

if __name__ == "__main__":
    play_game()
