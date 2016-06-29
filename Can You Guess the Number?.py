
import simplegui
import math
import random


number_guessed = 0
secret_number = 0
guess_remain = 0
# helper function to start and restart the game
def new_game():
    global secret_number
    global guess_remain
  
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is 7"
    secret_number = random.randrange(0, 100)
    guess_remain = 7
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global guess_remain
  
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is 7"
    secret_number = random.randrange(0, 100)
    guess_remain = 7
    print ""

def range1000():
    global secret_number
    global guess_remain 
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is 10"
    secret_number = random.randrange(0, 1000)
    guess_remain = 10
    print ""
    
    
def input_guess(guess):
    # main game logic 
    global number_guessed
    global guess_remain
   
    number_guessed = int(guess)
    print "Guess was", number_guessed
    guess_remain -= 1
    print "Number of remaining guess is", guess_remain
    
    if number_guessed == secret_number:
        print "Correct"
    elif number_guessed > secret_number:
        print "Lower"
    elif number_guessed < secret_number:
        print "Higher"
    else:
        print "Something is terribly wrong here!"
        
    print ""
        
    if guess_remain == 0:
        print "You have no more remaining guesses, Sorry You Lose!"
        print "Restarting Game!"
        print ""
        new_game()
    

    

frame = simplegui.create_frame("Guess the number", 200, 200)

frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game
frame.add_button("Restart", new_game, 200)

new_game()


