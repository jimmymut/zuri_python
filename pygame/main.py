import random
print("Welcome to Rock-Paper-Scissors game\nYou are going to play against the computer")
print("we have three options, you have to pick one for every move\nwhich are: 'R' for 'Rock', 'P' for 'Paper' and 'S' for 'Scissors'")
print("and the rules of the game are:\n\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper\n\nGood luck\n")

listoptions = ["R", "P", "S"]
Playercount = 0
CPUcount = 0
while Playercount < 3 or CPUcount < 3:
    while True:
        Player = str.upper(input("pick your move, either R or P or S:\n"))
        if Player not in listoptions:
            print("Error! picked a invalid option, try again")
            True
        CPU = random.choice(listoptions)
        if (Player == 'R' and CPU == 'R') or (Player == 'P' and CPU == 'P') or (Player == 'S' and CPU == 'S'):
            True
        if Player == 'R' and CPU == 'S':
            print("Player (Rock) : CPU (Scissors)")
            Playercount += 1
        elif Player == 'R' and CPU == 'P':
            print("Player (Rock) : CPU (Paper)")
            CPUcount += 1
        elif Player == 'P' and CPU == 'R':
            print("Player (Paper) : CPU (Rock)")
            Playercount += 1
        elif Player == 'P' and CPU == 'S':
            print("Player (Paper) : CPU (Scissors)")
            CPUcount += 1
        elif Player == 'S' and CPU == 'R':
            print("Player (Scissors) : CPU (Rock)")
            CPUcount += 1
        else:
            print("Player (Scissors) : CPU (Paper)")
            Playercount += 1
