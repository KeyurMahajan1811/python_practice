import random

roll = random.randint(1, 6)
guess = int(input("Guess what is dice no !!! \n"))

if(roll == guess):
    print("Correct!! How do you do that..They have rolled a"+str(roll))
else:
    print("Wrong!!They have rolled a"+str(roll))
