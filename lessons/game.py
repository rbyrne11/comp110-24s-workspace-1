"""Number Guessing Game"""
from random import randint

SECRET: int = randint(1,5)
correct: bool = False

while correct == False :
    guess: int = int(input("Guess a number: "))

    if guess == SECRET: 
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if guess > SECRET:
            print( "You're guess was too high! Try again.")
        if guess < SECRET:
            print( "You're guess was too low! Try again.")
        print("Try again!")
    

