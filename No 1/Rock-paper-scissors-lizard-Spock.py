Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Rock-paper-scissors-lizard-Spock

#http://www.codeskulptor.org/#user26_AkfrHoKGy2_4.py

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0: 
        name = "rock"
    elif number == 1: 
        name = "Spock"
    elif number == 2: 
        name = "paper"
    elif number == 3: 
        name = "lizard"
    elif number == 4: 
        name = "scissors"  
    else: 
        print("Not a valid number choice")
        
    return name
    
def name_to_number(name):
    # convert name to number using if/elif/else    
    if name == "rock": 
        number = 0
    elif name == "Spock": 
        number = 1
    elif name == "paper": 
        number = 2
    elif name == "lizard": 
        number = 3
    elif name == "scissors": 
        number = 4   
    else: 
        print("Bad input!")
        
    return number

def rpsls(name): 
    # convert name to player_number using name_to_number
    # compute random guess for comp_number using random.randrange()
    # compute difference of player_number and comp_number modulo five
    # convert comp_number to name using number_to_name  
    player_num = name_to_number(name)
    
    comp_num = random.randrange(5)
       
    math_result = (player_num - comp_num) % 5
    
    if math_result == 0:
        result = "Player and computer tie!"
    if math_result == 1 or math_result == 2:
        result = "Player wins!"
    if math_result == 3or math_result == 4:
        result = "Computer wins!"
   
    player_name = number_to_name(player_num)
    comp_name = number_to_name(comp_num)
        
    print("Player chooses "+ player_name)
    print("Comp chooses "+ comp_name)
    print(result)
    print
      
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
