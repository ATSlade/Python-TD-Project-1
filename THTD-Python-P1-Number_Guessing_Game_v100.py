"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
MasonB Submission
--------------------------------
"""

#I'm just looking for a passing score. Any of the "extras" I achieved will just serve to make me happier :)

import random


def start_game():
    
    high_score = 10
    print("Welcome to Guess-That-Number!!! The high score is {}. ".format(high_score))
    
    compliance = input("Do you want to play? [y]es, [n]o ? ")
    
    while compliance.lower() == "y":
        try:
                
            rand_number = random.randint(1, 10)
            guesses = 0
            if guesses == 0:
                high_score == 10
            elif guesses > 0:
                high_score = guesses
            guess = int(input("Guess a number between 1 and 10! Try to beat the current high score of {}! ".format(high_score)))
                
            while guess != rand_number:
                try:
                    guess = int(guess) 
                    if guess > 10:
                        print("\nSorry! That value is above the specified range.\n")
                        guess = int(input("Please try again. Guess a number between 1 and 10! "))
                        guesses += 1
                               
                    elif guess < 1:
                        print("\nSorry! That value is below the specified range.\n") 
                        guess = int(input("Please try again. Guess a number between 1 and 10! "))
                        guesses += 1
                    
                    elif guess < rand_number:
                        guess = int(input("That's too low. Try again. "))
                        guesses += 1
                        
                    elif guess > rand_number:
                        guess = int(input("That's too high. Try again. "))
                        guesses += 1
                        
                    if guess == rand_number:
                            guesses += 1
                            print("\nYou got it, and it only took you {} attempts. Great job! \n".format(guesses))
                            compliance = input("Game Over. Do you want to play again and try for a better score than {} guesses? [y]es [n]o? ".format(guesses))
                            high_score = guesses
                            
                except ValueError:
                    print("\nOh no! Our system encountered an error. Check and make sure that the values you submit are integers between 1 and 10.\n")
                    guess = input("Please try again. Choose an integer between 1 and 10. ")
                    
        except ValueError:
            print("\nOh no! Our system encountered an error. Please enter a valid value.")
    else:
        exit()
    

if __name__ == '__main__':
    start_game()