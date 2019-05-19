# Acie Slade - # Project 1 (Number Guessing Game)

import random

print('''
---------------------------------
Welcome to the Number Guess Game!
---------------------------------
    
Let's begin!

I will choose a secret number between and including the numbers 1 and 10, and you will try to guess the number.
For both of our parts, our numbers will be integers not decimals or a floats.
I will track how many guesses it takes, and together we will see if you can beat the "high-score" of the fewest guesses.

At the prompt, you can enter 'x' to exit/quit, if you'd like.
''') 

def start_game():
    play = True
    best_score = 10
    guess_count = 0
    rando = random.randint(1, 10) # RANDOM NUMBER GEN referenced http://pythonspot.com/random-numbers/
    print("\nOk...I have my secret number.\n")    
    
    while play is True:
        player_guess = input("What's your guess?: ")
        if player_guess.lower() == 'x':
            print("\nOk...good-bye!")
            break
        else:
            try:
                player_guess = int(player_guess)
            except ValueError:
                print("Invalid entry. Please choose an INTEGER NUMBER between and including 1 and 10: ")
                continue
            guess_count += 1    
            if player_guess == rando:
                    if guess_count < best_score:
                        best_score = guess_count 
                        print("Got it! And we have a new best score of {} tries.\n".format(guess_count))
                    else:
                        print("Got it! It only took {} guesses, but you did not beat the best score.\n".format(guess_count))
                    play_again = input("Would you like to play again? 'y' for yes, 'n' for no: ")                   
                    if play_again.lower() == 'y':
                        guess_count = 0
                        rando = random.randint(1, 10)                            
                    else:                        
                        print("Okie dokie then...good-bye!\n")
                        break                
            elif player_guess > rando and player_guess <= 10:
                print("The secret number is lower. Please try again.")
            elif player_guess < rando and player_guess >= 1:
                print("The secret number is higher. Please try again.")
            else:
                print("That guess is outside the range and won't count against you. Please try again.")
                guess_count -= 1   

if __name__ == '__main__':
    start_game()