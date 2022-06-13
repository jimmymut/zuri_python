from multiprocessing import cpu_count
import random
from this import d
print("Welcome to Rock-Paper-Scissors game\nYou are going to play against the computer")
print("we have three options, you have to pick one for every move\nwhich are: 'R' for 'Rock', 'P' for 'Paper' and 'S' for 'Scissors'")
print("and the rules of the game are:\n\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper\n\nGood luck\n")

listoptions = ["R", "P", "S"]
Playercount = 0
CPUcount = 0
while True:
    Player = input("pick your move, either R or P or S:\n").upper()
    while Player not in listoptions:          
        Player = input("Error! picked a invalid option, try again\nplease pick either R or P or S:\n").upper()
    CPU = random.choice(listoptions)
    if Player == CPU:
        print("its a tie, repeat")
        continue
    elif Player == 'R' and CPU == 'S':
        print("Player (Rock) : CPU (Scissors)")
        Playercount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    elif Player == 'R' and CPU == 'P':
        print("Player (Rock) : CPU (Paper)")
        CPUcount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    elif Player == 'P' and CPU == 'R':
        print("Player (Paper) : CPU (Rock)")
        Playercount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    elif Player == 'P' and CPU == 'S':
        print("Player (Paper) : CPU (Scissors)")
        CPUcount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    elif Player == 'S' and CPU == 'R':
        print("Player (Scissors) : CPU (Rock)")
        CPUcount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    else:
        print("Player (Scissors) : CPU (Paper)")
        Playercount += 1
        print("wins %d:%d" % (Playercount, CPUcount))
    winner = False
    if Playercount != CPUcount and (Playercount == 3 or CPUcount == 3):
        if Playercount > CPUcount and Playercount == 3:
            print("The Player is the winner\nThank you for playing this game")
            break
        else:
            print("The CPU is the winner\nThank you for playing this game")
            break
