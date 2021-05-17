import random

com_choise = random.choice(['Scissors', 'Rock', 'Paper'])
print(com_choise)

user_choice = input("What do you want to pick: Rock, Paper and Scissors")

if(com_choise == user_choice):
    print("TIE!!!")
elif user_choice == "Rock" and com_choise == "Scissors":
    print("WIN!!!")
elif user_choice == "Paper" and com_choise == "Rock":
    print("WIN!!!")
elif user_choice == "Scissors" and com_choise == "Paper":
    print("WIN!!!")
else:
    print("You Lose!!(Computer Wins)")
