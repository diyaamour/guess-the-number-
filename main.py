from random import randint 
from art import logo 

EASY_LEVEL = 10 
HARD_LEVEL = 5 

def check_answer(guess, answer, turns):
    if guess > answer: 
        print("Too high. 👇")
        return turns - 1 
    elif guess < answer: 
        print("Too low. 👆")
        return turns - 1 
    else:
        print(f"You guessed right. The answer is {answer}")

def set_difficulty():
    
    level = input("Choose the game's level of difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL
    else: 
        return HARD_LEVEL 

def game():
    print(logo)
    print("Let's play a game of guessing numbers")
    print(" I have a number between 1 and 100 in mind. Guess what it is. 🧐 ")
    answer = randint(1, 100)
    print(f"The answer is: {answer}")
    turns = set_difficulty()

    guess = 0 

    while guess != answer: 
        print(f"You have {turns} guesses left. ")

        guess = int(input("Type your guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You ran out of guesses. Game Over!")
            return 
        elif guess != answer: 
            print("Guess Again.")
game()
        
