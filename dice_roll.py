import random


def roll_dice():
    total_count = random.randint(1, 6)+random.randint(1, 6)
    return total_count


no_of_player = int(input("How many players are playing ?"))

players = []
winner = 'none'

if no_of_player <= 1:
    print("Players should be more than 1.")
else:
    for i in range(no_of_player):
        print("Type Player", i, " Name: ", sep="")
        players.append(input(""))
    max = 0
    tie_flag = 0
    for j in range(no_of_player):
        dice_cnt = roll_dice()
        print(players[j], " Rolled: ", dice_cnt, sep="")
        if max < dice_cnt:
            max = dice_cnt
            winner = players[j]
        elif max <= dice_cnt:
            tie_flag = 1
            winner = winner+" And "+players[j]

if tie_flag != 1:
    print(winner, "is the winner with roll dice", max)
else:
    print("This is Tie Between", winner)
