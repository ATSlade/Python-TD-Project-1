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

    else:

#    while (status < 1) or (status > 2):
#        print('Invalid entry. Please enter "1" to play, or "2" to quit.')
#        status = (input('Enter choice: '))
#        status = int(status)

# SET-UP loop
while status == 1:
player_name = input('\nHello. With whom do I have the pleasure of playing with today? (Enter your first name): ')
print('\nThank you, {}.'.format(player_name))
print('''
Let's begin!
I will choose a secret number between and including the numbers 1 and 10, and you will try to guess the number.
I will track how many guesses it takes, and together we will see if you can beat the "high-score" of the fewest guesses.
''')
rando = random.randint(1, 10)
print('Ok...I have chosen my secret number!')
guess_count = 0        
correct = False  # sets up the PLAY loop below
# PLAY loop
while correct == False:
user_guess = input("\nWhat's your guess?: ")
guess_count += 1

if int(user_guess) > rando:
print('The secret number is lower.')
elif int(user_guess) < rando:
print('The secret number is higher.')
else:
print("\nGot it! And it only took you {} guesses.".format(guess_count))
correct = True
# REPLAY
print('\nPlay again? Enter "1" to play, or "2" to quit.')
status = int(input('Enter choice: '))
while (status < 1) or (status > 2):
print('Invalid entry. Please enter "1" to play, or "2" to quit.')
status = int(input('Enter choice: '))
# "RE-ROLL" or END GAME
if status == 1:
    rando = random.randint(1, 10)
    print('Ok...I have chosen my secret number!') # transition from game "set-up" to game "play" 
    guess_board = []
    guess_count = 0
    correct = False  # sets up the PLAY loop
else:
    correct = True
    print('\nThe Number Guessing game is now over') 
       
print('Good-bye!\n')                    
print('Good-byeeeee!\n') 

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()