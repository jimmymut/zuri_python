from multiprocessing import cpu_count
import random
print("Welcome to Rock-Paper-Scissors game\nYou are going to play against the computer")
print("we have three options, you have to pick one for every move\nwhich are: 'R' for 'Rock', 'P' for 'Paper' and 'S' for 'Scissors'")
print("and the rules of the game are:\n\nRock beats Scissors\nPaper beats Rock\nScissors beats Paper\n\nGood luck\n")

listoptions = ["R", "P", "S"]
Playercount = 0
CPUcount = 0
Playerwins = 0
CPUwins = 0
while True:
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
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        elif Player == 'R' and CPU == 'P':
            print("Player (Rock) : CPU (Paper)")
            CPUcount += 1
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        elif Player == 'P' and CPU == 'R':
            print("Player (Paper) : CPU (Rock)")
            Playercount += 1
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        elif Player == 'P' and CPU == 'S':
            print("Player (Paper) : CPU (Scissors)")
            CPUcount += 1
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        elif Player == 'S' and CPU == 'R':
            print("Player (Scissors) : CPU (Rock)")
            CPUcount += 1
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        else:
            print("Player (Scissors) : CPU (Paper)")
            Playercount += 1
            print("wins {:d}:{:d}".format(Playercount, CPUcount))
        winner = False
        if Playercount != CPUcount and (Playercount == 3 or CPUcount == 3):
            if Playercount > CPUcount and Playercount == 3:
                Playerwins += 1
                print("You are the winner")
                break
            else:
                CPUwins += 1
                print("CPU is the winner")
                break
    repeat = input("Do you want to play again?\nType 'yes/y' to play again or 'no/n' to quit the game\n").upper()
    while not(repeat == 'YES' or repeat == 'Y' or repeat == 'NO' or repeat == 'N'):
        repeat = input("invalid input!\nplease type yes/y to keep playing or\nType No/n to Quit the game\n").upper()
    if repeat == 'YES' or repeat == 'Y':
        Playercount = 0
        CPUcount = 0
    else:
        print("Played games = {:d}\n".format(Playerwins + CPUwins))
        print("You won {:d} times".format(Playerwins))
        print("CPU won {:d} times".format(CPUwins))
        print("Thank you for playing this game!\nGood bye! Have a nice time!")
        break