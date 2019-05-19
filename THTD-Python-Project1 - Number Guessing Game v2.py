"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )

    MUST HAVES:
    Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
    As a player of the game, I should see a some kind of text header, welcome or game intro message, before or above the menu.
    As a player of the game, I should be continuously prompted for a guess until I get it right.
    As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
    As a player of the game, after the game ends I should be shown my number of attempts at guessing.

    EXTRA CREDIT:
    As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
    As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    As a player of the game, at the start of each game I should be shown the current high score (least amount of points [guesses?]), so that I know what I am supposed to beat.

    """
import random

def start_game():
# Greet the player and explain the game
    player_name = input('Hello. With whom do I have the pleasure of playing with today? (Enter your first name): ')
    print('\nThank you, {}. Welcome to the Number Guessing game!'.format(player_name))
    print('''
        I will choose a random number between and including the numbers 1 and 10.
        You will try to guess that number, and I will track how many guesses it takes you to accomplish this.
        See if you can beat the high-score!
    ''')

    # Have Python create a random number and store it
    rando = random.randint(1, 10)
    guess_board = []
    
    print('Ok...I have chosen my secret number!') # transition from game "set-up" to game "play" 
    correct = False  # sets up the loop

    guess_count = 0
    # On a loop, prompt the player to 'guess' the number
    while correct == False:
        # TO DO -- probably a function here --
        user_guess = input("\nWhat's your guess?: ")
        guess_count += 1
        # If guess is greater, display "It's lower"
        if int(user_guess) > rando:
            print('The secret number is lower. Guess again.')
        # If guess is less, display "It's higher"
        elif int(user_guess) < rando:
            print('The secret number is higher. Guess again')
        # If guess = rando, display "Got it"
        else:
            print("Got it! And it only took you {} guesses.".format(guess_count))
            correct = True

print("\nThe Number Guessing game is now over. Thanks for playing, {}!\n".format(player_name))        
        # Display how many guesses were consumed by the player
        # Inform player that the game is over
    # Include error on invalid guess (outside the range OR if a string OR if a symbol)
    # Warn the player about a repeated guess
        

    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()