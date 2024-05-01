#rock-paper-scissor 
import random
a = input("Enter your ans: ")
computer_choice = random.choice(["rock", "paper", "scissors"])
print("computer chose:", computer_choice)

if a == computer_choice:
    print("Draw")
elif a == "rock" and computer_choice == "scissors":
    print("You WON")
elif a == "paper" and computer_choice == "rock":
    print("You WON")
elif a == "scissors" and computer_choice == "paper":
    print("You WON")
else:
    print("YOU LOST WEH WEH WEHHHHHHHH")
   


    
