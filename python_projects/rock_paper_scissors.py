
''' Rock Paper Scissors'''
''' user will choose from three of them and computer will randomly select one from the three and the rules are:

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins'''

import random

li = ["rock", "paper", "scissor"]


while True:
    user_input = input("Rock or Paper or Scissor: ").lower()
    computer_input = random.choice(li)
    if user_input == "rock" and computer_input == "rock":
        print("Tie")
       
    if user_input == "rock" and computer_input == "paper":
        print("You lose")
    
    if user_input == "rock" and computer_input == "scissor":
        print("You win")
    
    if user_input == "paper" and computer_input == "rock":
        print("You win")
    
    if user_input == "paper" and computer_input == "paper":
        print("Tie")
    
    if user_input == "paper" and computer_input == "scissor":
        print("You lose")
    
    if user_input == "scissor" and computer_input == "rock":
        print("You lose")
    
    if user_input == "scissor" and computer_input == "paper":
        print("You win")
    
    if user_input == "scissor" and computer_input == "scissor":
        print("Tie")
    
    print("Do you want to Play again?")
    ans = input().lower

    if ans == "yes":
        continue
    else: 
        break
       


