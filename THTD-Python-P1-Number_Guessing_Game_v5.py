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
    status = 0

    while (status != 1) or (status != 2):
        status = input('\nEnter "1" to play, or "2" to quit: ')

        try:
            status = int(status)
            if (status < 1) or (status > 2):
                raise ValueError('Please enter "1" to play, or "2" to quit: ')
        except ValueError as err:
            print("We have an issue: {} \n".format(err))
            elif status == 1:
                print('Playing...')
            else:
                print('Quiting...')        


       
print('Good-bye!\n')                    
print('Good-byeeeee!\n') 

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()