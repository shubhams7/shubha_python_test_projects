import random

options=["rock","paper","scissors"]
My_score=0
Comp_score=0
while True :
    user_input = input("Please input either rock/paper/scissors/Quit : ").lower()
    computer_pick= options[random.randint(0,2)]
    if user_input == "quit":
        break
    elif user_input == "rock" and  computer_pick == "scissors":
        print("You won")
        My_score+=1
    elif user_input == "paper" and  computer_pick == "rock":
        print("You won")
        My_score+=1
    elif user_input == "scissors" and  computer_pick == "paper":
        print("You won")
        My_score+=1
    else:
        print("You lost")
        Comp_score+=1

print( "The total score is", My_score ,  "." )
    

