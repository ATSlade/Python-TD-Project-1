"""EXTRA CREDIT:
As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
As a player of the game, after I guess correctly I should be prompted if I would like to play again.
As a player of the game, at the start of each game I should be shown the current high score (least amount of points [guesses?]), so that I know what I am supposed to beat.
"""

import random

def start_game():
# TITLE and MENU
    print('''
    ---------------------------------
    Welcome to the Number Guess Game!
    ---------------------------------
    
    Let's begin!
    I will choose a secret number between and including the numbers 1 and 10, and you will try to guess the number.
    I will track how many guesses it takes, and together we will see if you can beat the "high-score" of the fewest guesses.
    ''') 

# INITIALIZE GAME *OR* QUIT
    correct = False
    guess_count = 0
    best_score = 10

    start_command = input("Shall we play? Please enter 'y' for yes or 'n' for no: ")

    while correct == False:
        while start_command.lower() == 'y':
            try:
                rando = random.randint(1, 10) # RANDOM NUMBER GEN referenced http://pythonspot.com/random-numbers/
                print('Ok...I have chosen my secret number!\n')
                print(rando)  
    #        try:
                player_guess = int(input("What's your guess?: "))

                while player_guess != rando:
                    try:    
                        player_guess = int(player_guess)
                        guess_count += 1
                        if player_guess < 1 or player_guess > 10:
                            player_guess = input("Invalid entry. Please pick a number between and including 1 and 10: ")
                            player_guess = int(player_guess)
                            guess_count -= 1
                        elif player_guess > rando:
                            player_guess = input("The secret number is lower. Please guess again: ")
                            player_guess = int(player_guess)   
                        else:
                            player_guess = input("The secret number is higher. Please guess again: ")
                            player_guess = int(player_guess)
                    except ValueError:
                        print('Invalid entry. Numbers only, please!')    
                        player_guess = input("For your guess, enter a number between and including '1' and '10': ")

                while player_guess == rando:
                    correct == True
                    guess_count += 1
                    if guess_count < best_score:
                        best_score = guess_count
                        print('Got it! And we have a new best score of {} guesses!\n'.format(best_score))
                    else:
                        print('Got it! It only took you {} guesses, but you did not beat the best score of {} guesses.\n'.format(guess_count, best_score))        
                    
                correct == False
                start_command = input('Would you like to play again?')                

                if 

            except ValueError:
                print("Wrong!!!")           
                        
    while start_command.lower() == 'n':
        print("Ok. Goodbye!\n")


if __name__ == '__main__':

    start_game()              