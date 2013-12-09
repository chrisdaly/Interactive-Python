Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import simplegui
import random
import math

# initialize global variables used in your code
secretnumber = 0
userinput = 0
numrange = 100
guesses = 7
temp_guess = 0

# helper function to start and restart the game
def new_game():
    global secretnumber, guesses, temp_guess
    temp_guess = guesses
    secretnumber = random.randrange(0,numrange)
    
    print "New game. Range is from 0 to", numrange
    print "Number of remaining guesses is", guesses
    print
    pass

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global numrange, guesses
    numrange = 100
    guesses = 7 
    new_game() 
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global numrange, guesses
    numrange = 1000
    guesses = 10
    new_game()
    pass
    
def input_handler(text):
    # main game logic goes here	
    global guess, secretnumber, guesses, temp_guess
    guess = int(text)
    inp.set_text('')
    
    print "Guess was", guess
   
    if guess != secretnumber:
        temp_guess = temp_guess -1
        
    print "Number of remaining guesses is", temp_guess
    
    if guess > secretnumber:
        print "Lower!"
        print

    if guess < secretnumber:
        print "Higher!"
        print
        
    if guess == secretnumber:
        print "Correct!"
        print
        new_game()
    
    if temp_guess == 0:
        print "You lose!"
        print "The correct number was", secretnumber
        print
        new_game()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# create control elements
frame.add_button("Range is [0, 100]", range100, 150)
frame.add_button("Range is [0, 1000]", range1000, 150)
inp = frame.add_input("Enter a guess:", input_handler, 100)

# call new_game and start frame
new_game()
