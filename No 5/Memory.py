Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # implementation of card game - Memory
import simplegui
import random
cards = []
exposed = []
CARD_WIDTH = 50
CARD_HEIGHT = 100
state = 0
counter = 0
first_pos, first_val, second_pos, second_val = 0,0,0,0

# helper function to initialize globals
def new_game():
    global cards, exposed, counter
    counter = 0
    cards = range(8)*2 
    exposed = [False for x in range(16)]
    random.shuffle(cards)
  
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, counter
    global first_pos, first_val, second_pos, second_val
         
    if state == 0:
        first_pos = pos[0]//50
        first_val = cards[first_pos]
        
        if exposed[first_pos] == True:
            state = 0
        
        else:
            exposed[first_pos] = True
            state = 1 
    
    elif state == 1:
        second_pos = pos[0]//50
        second_val = cards[second_pos]
  
        if exposed[second_pos] == True:
            state = 1
        
        else:
            exposed[second_pos] = True
            
            counter += 1
            label.set_text("Moves = " + str(counter))
        state = 2

    elif state ==2:

        if first_val != second_val:
            exposed[first_pos], exposed[second_pos] = False, False

        else:
            exposed[first_pos], exposed[second_pos] = True, True
            
        state = 0
                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    global CARD_WIDTH, CARD_HEIGHT
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_line(((i*CARD_HEIGHT/2 + CARD_WIDTH/2),0), ((i*CARD_HEIGHT/2 + CARD_WIDTH/2),100), 48, "Black")
            canvas.draw_text(str(cards[i]), [i*CARD_HEIGHT/2 + CARD_WIDTH/2/1.8, 60], 40, "White")
        
        else:
            canvas.draw_line(((i*CARD_HEIGHT/2 + CARD_WIDTH/2),0), ((i*CARD_HEIGHT/2 + CARD_WIDTH/2),100), 48, "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()