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
    ''')
# INITIALIZE GAME *OR* QUIT
    guess_count = 0
    best_score = 10
    legit_values = [1, 2]
    play_or_quit = True

    while play_or_quit == True:
        user_value = (input("Please enter '1' to play or '2' to quit: "))
        try:                
            play_or_quit = int(user_value)
        except:
            print("That's not a valid entry. Please use '1' or '2' only.")
        if play_or_quit == 2:            
            print("Bye-Bye!")
            break
        elif play_or_quit == 1:
            continue
        else:
            continue    


#            play_or_quit = int(input('Please enter "1" to play or "2" to quit: '))
#            if play_or_quit not in (legit_values):
#                print("That's an invalid entry. Please enter '1' to play or '2' to quit: ")
#            else:
#                break

# CATCH ERRORS

        while play_or_quit == 1:
            print('''
        Let's begin!
        I will choose a secret number between and including the numbers 1 and 10, and you will try to guess the number.
        I will track how many guesses it takes, and together we will see if you can beat the "high-score" of the fewest guesses.
            ''')

    # GENERATE THE RANDOM NUMBER and SET UP THE PLAY LOOP
            rando = random.randint(1, 10) # RANDOM NUMBER GEN referenced http://pythonspot.com/random-numbers/
            print('Ok...I have chosen my secret number!\n')
            print(rando)  
            correct = False  # sets up the PLAY loop
            guess_count = 0 # 2nd instance of guess_count, DO I NEED THIS???
            proceed = True

            while proceed == True:   
            
                try:
                    player_guess = (input("What's your guess?: \n"))
                    player_guess = int(player_guess)
                                    
                    while correct == False:
                        guess_count += 1
                        if player_guess < 1 or player_guess > 10:
                            player_guess = input("That's an error. Please pick a number between and including 1 and 10: ")
                            player_guess = int(player_guess)
                            guess_count -= 1
                        elif player_guess > rando:
                            player_guess = input("The secret number is lower. Please guess again: ")
                            player_guess = int(player_guess)   
                        elif player_guess < rando:
                            player_guess = input("The secret number is higher. Please guess again: ")
                            player_guess = int(player_guess)
                        elif player_guess == rando:
                            correct = True
                        else:
                            #type(player_guess) == str or type(player_guess) == float
                            raise ValueError("That's an invalid entry.")
                except ValueError:
                    player_guess = input("You didn't enter an number. Please try again and pick a number between and including 1 and 10: ")    

                if guess_count < best_score:
                    best_score = guess_count
                    print("Got it! And we have a new best score of {} guess(es)!\n".format(best_score))
                else:
                    print("Got it! It only took you {} guesses, but you did not beat the best score of {} guess(es).\n".format(guess_count, best_score))
                    
                player_restart = input("Play again? Enter '1' to play or '2' to quit: ")
                player_restart = int(player_restart)
                if player_restart == 2:
                    proceed = False
                    play_or_quit = 2
                elif player_restart == 1:    
                    play_or_quit = 1
                    rando = random.randint(1, 10) # RANDOM NUMBER GEN referenced http://pythonspot.com/random-numbers/
                    print('\nOk...I have chosen another secret number!')
                    print(rando)
                    guess_count = 0
                    correct = False  
                else:
                    player_restart = input("That's an invalid entry. Would you like to play again? Enter '1' to play or '2' to quit ")
       # ---> need to catch error of a big number here <---- #
        while play_or_quit == 2:
            print("Goodbye!\n")
            break


if __name__ == '__main__':

    start_game()              