# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_vel, paddle2_vel = 0, 0

speed_factor = 1
paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2
paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2
        
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global speed_factor
    ball_vel = [0,0]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    speed_factor = 1
    
    if direction == RIGHT:
        ball_vel[0], ball_vel[1] = random.randrange(3,7), -random.randrange(2,5)
    if direction == LEFT:
        ball_vel[0], ball_vel[1] = -random.randrange(3,7), -random.randrange(2,5)
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = "0"
    score2 = "0"
    spawn_ball(RIGHT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global speed_factor
    speed = 4
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # Collision
    # LHS
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] - BALL_RADIUS > paddle1_pos + PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS < paddle1_pos):
            score2 = str(int(score1)+1)
            spawn_ball(RIGHT)
         
    # RHS
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] - BALL_RADIUS > paddle2_pos + PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS < paddle2_pos):
            score1 = str(int(score1)+1)
            spawn_ball(LEFT)
            
    # collide and reflect off of left hand side of canvas
    # Left paddle
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]  
        speed_factor = 1.1*speed_factor
        print speed_factor
        
    # Right paddle
    if ball_pos[0] >= WIDTH -1 -BALL_RADIUS:
        ball_vel[0] = - ball_vel[0] 
        speed_factor = 1.1*speed_factor
        print speed_factor
        
    # Top wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # Bottom wall
    if ball_pos[1] >= HEIGHT - 1- BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # update ball
    ball_pos[0] += ball_vel[0]*speed_factor
    ball_pos[1] += ball_vel[1]*speed_factor
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
   
    # update paddle's vertical position, keep paddle on the screen
    # paddle #1
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0:
        paddle1_pos = 0
        
    elif paddle1_pos >= HEIGHT - 1 - PAD_HEIGHT:
        paddle1_pos = HEIGHT - 1 - PAD_HEIGHT
    
    # paddle #2
    paddle2_pos += paddle2_vel
    if paddle2_pos <= 0:
        paddle2_pos = 0
        
    elif paddle2_pos >= HEIGHT - 1 - PAD_HEIGHT:
        paddle2_pos = HEIGHT - 1 - PAD_HEIGHT
    
    # draw paddles
    paddle_1 = c.draw_line((PAD_WIDTH/2, paddle1_pos), (PAD_WIDTH/2, paddle1_pos + PAD_HEIGHT), PAD_WIDTH, 'White')
    paddle_2 = c.draw_line((WIDTH -1 - PAD_WIDTH/2, paddle2_pos), (WIDTH -1 - PAD_WIDTH/2, paddle2_pos + PAD_HEIGHT), PAD_WIDTH, 'White')
   
    # draw scores
    player1_score = c.draw_text(score1, (250,100), 40, "Red")
    player2_score = c.draw_text(score2, (330,100), 40, "Red")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    pad_speed = 7
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_speed 
        
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= pad_speed 
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += pad_speed 
        
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= pad_speed 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 150)


# start frame
new_game()
frame.start()
