"""EXTRA CREDIT:
As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
As a player of the game, after I guess correctly I should be prompted if I would like to play again.
As a player of the game, at the start of each game I should be shown the current high score (least amount of points [guesses?]), so that I know what I am supposed to beat.
"""

import random

def start_game():
# Greet the player and explain the game
    print('''
    ---------------------------------
    Welcome to the Number Guess Game!
    ---------------------------------
    ''')
    
    print('\nEnter "1" to play, or "2" to quit.')
    status = int(input('Enter choice: '))

    while (status < 1) or (status > 2):
        print('Invalid entry. Please enter "1" to play, or "2" to quit.')
        status = int(input('Enter choice: '))

    # Here is the SET-UP loop
    while status == 1:
        player_name = input('\nHello. With whom do I have the pleasure of playing with today? (Enter your first name): ')
        print('\nThank you, {}.'.format(player_name))
        print('''
    Let's begin!

    I will choose a secret number between and including the numbers 1 and 10, and you will try to guess the number.
    I will track how many guesses it takes, and together we will see if you can beat the "high-score" of the fewest guesses.
        ''')

        # Have Python create a random number and store it
        rando = random.randint(1, 10)
        guess_board = []

        print('Ok...I have chosen my secret number!') # transition from game "set-up" to game "play" 
        correct = False  # sets up the PLAY loop

        guess_count = 0
    
        # Here's is the PLAY loop
        while correct == False:
            # TO DO -- probably a function here --
            user_guess = input("\nWhat's your guess?: ")
            guess_count += 1
            # If guess is greater, display "It's lower"
            if int(user_guess) > rando:
                print('The secret number is lower.')
            # If guess is less, display "It's higher"
            elif int(user_guess) < rando:
                print('The secret number is higher.')
            # If guess = rando, display "Got it"
            else:
                print("\nGot it! And it only took you {} guesses.".format(guess_count))
                correct = True

                print('\nPlay again? Enter "1" to play, or "2" to quit.')
                status = int(input('Enter choice: '))
                while (status < 1) or (status > 2):
                    print('Invalid entry. Please enter "1" to play, or "2" to quit.')
                    status = int(input('Enter choice: '))
                #correct = False

                rando = random.randint(1, 10)
                guess_board = []
                guess_count = 0
                print('Ok...I have chosen my secret number!') # transition from game "set-up" to game "play" 
                correct = False  # sets up the PLAY loop


    




    #status = input("\nWould you like to continue, {}? Enter '1' for 'Yes' and '2' for 'No': ".format(player_name)) 

    #if status == 1:

    print("\nThe Number Guessing game is now over. Thanks for playing, {}!\n".format(player_name))        
        # Display how many guesses were consumed by the player
        # Inform player that the game is over
    # Include error on invalid guess (outside the range OR if a string OR if a symbol)
    # Warn the player about a repeated guess
        

    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()