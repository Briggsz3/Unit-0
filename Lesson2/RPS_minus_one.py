'''
Name: Zachary Briggs
File: rps_minus_one.py
Description: implements the rock paper scissor minus one from Squid Game.
'''

"""
Pseudocode
Have computer pick two randome "hands" of rps
SET comp score and player score to 0
STORE values in comp_hand
ASK user for their hands
STORE their hands 
ASK user what hand to keep
computer random generate for what hand to choose
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and END game
ELSE play again
"""
import random
score = 0
comp_score = 0
while True:
    comp_rps1 = random.randint(1,3)
    comp_rps2 = random.randint(1,3)
    comp_minus_1 = random.randint(1,2)
    start = int(input("Would you like to end the game (1) or start the game (2): "))
    if start == 2:
        if comp_rps1 == 1:
            comp_hand1 = 'rock'
        elif comp_rps1 == 2:
            comp_hand1 = 'paper'
        else:
            comp_hand1 = 'scissors'
        
        if comp_rps2 == 1:
            comp_hand2 = 'rock'
        elif comp_rps2 == 2:
            comp_hand2 = 'paper'
        else:
            comp_hand2 = 'scissors'
        hand1 = int(input("What would you like hand 1 to be rock (1), paper (2), or scissors (3):"))
        if hand1 == 1:
            user_hand1 = 'rock'
        elif hand1 == 2:
            user_hand1 = 'paper'
        else:
            user_hand1 = 'scissors'
        hand2 = int(input("What would you like hand 2 to be rock (1), paper (2), or scissors (3):"))
        if hand1 == 1:
            user_hand2 = 'rock'
        elif hand1 == 2:
            user_hand2 = 'paper'
        else:
            user_hand2 = 'scissors'
        print(" ")
        print(f"The computers first hand is {comp_hand1} and their second hand is {comp_hand2}")
        print(" ")
        minus_1 = int(input("What hand would you like to take away, hand 1 (1), or hand 2 (2): "))
        if minus_1 == 1:
            u_mainhand = user_hand2
        else:
            u_mainhand = user_hand1
        if comp_minus_1 == 1:
            main_hand = comp_hand1
        else:
            main_hand = comp_hand2
        print(f"You chose {u_mainhand} and the computer chose {main_hand}")
        if main_hand == 'rock' and u_mainhand == 'rock':
            score = score
            comp_score = comp_score
            print("It's a draw")
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'rock' and u_mainhand == 'paper':
            score = score + 1
            comp_score = comp_score
            print("You won")
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'rock' and u_mainhand == 'scissors':
            print("You lost")
            score = score
            comp_score = comp_score +1
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'paper' and u_mainhand == 'rock':
            print("You lost")
            score = score
            comp_score = comp_score + 1
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'paper' and u_mainhand == 'paper':
            print('Its a draw')
            score = score
            comp_score = comp_score
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'paper' and u_mainhand == 'scissors':
            print('You win')
            score = score + 1
            comp_score = comp_score
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'scissors' and u_mainhand == 'rock':
            print('You win')
            score = score + 1
            comp_score = comp_score
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        elif main_hand == 'scissors' and u_mainhand == 'paper':
            print('You lose')
            score = score
            comp_score = comp_score + 1
            print(f"The score is you: {score} computer: {comp_score}")
            continue
        else:
            print("It's a draw")
            score = score
            comp_score = comp_score
            print(f"The score is you: {score} computer: {comp_score}")
            continue
    else:
        break

#show computers
#take away one remove from list
#show what computer took away
#if user == rock and etc...
#
