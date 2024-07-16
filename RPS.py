# Creating a Rock Paper Scissors game with python
# Program is going to accept input from the user and the computer 
# Program will check who wins

import random

user_score=0
computer_score=0
options = ['rock','paper','scissors']

def user():
    user_input  = input("ROCK | PAPER | SCISSORS \nChoose one: ").lower()
    if user_input not in options:
        print("Input the right option")
    else:
        return user_input
def computer():
    computer_choice = random.randint(0,2)
    computer_input = options[computer_choice]

    return computer_input


while True:

    continue_game = input("\nPress 'Enter' to continue game or 'Q' to quit game: ")
    if  continue_game == "q":
        if user_score == 0:
            print("GOODBYE!")
        else:
            print(f"You score: {user_score} | Computer Score: {computer_score}\nGOODBYE!")
        break
    else:
        # user()
        # computer()
        
        computer_option = computer()
        user_option = user()

        if user_option == "rock" and computer_option == "scissors":
            user_score +=1
            print(f"You Won! - You: {user_option} | Computer: {computer_option}")

        elif user_option == "paper" and computer_option == "rock":
            user_score +=1
            print(f"You Won! - You: {user_option} | Computer: {computer_option}")

        elif user_option == "scissors" and computer_option == "paper":
            user_score +=1
            print(f"You Won! - You: {user_option} | Computer: {computer_option}")

        elif user_option == "scissors" and computer_option == "scissors":
            user_score = user_score
            computer_score = computer_score
            print(f"ITS A TIE! - You: {user_option} | Computer: {computer_option}")

        elif user_option == "paper" and computer_option == "paper":
            user_score = user_score
            computer_score = computer_score
            print(f"ITS A TIE! - You: {user_option} | Computer: {computer_option}")

        elif user_option == "rock" and computer_option == "rock":
            user_score = user_score
            computer_score = computer_score
            print(f"ITS A TIE! - You: {user_option} | Computer: {computer_option}")

        else:
            computer_score +=1
            print(f"You Lost - You: {user_option} | Computer: {computer_option}")