import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

def play_rps():
        playerchoice = input(
            "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        if playerchoice not in ["1","2","3"]:
            print("You must enter 1, 2,or 3.")
            return play_rps()

        player = int(playerchoice)

        if player <1 or player >3:
            sys.exit("You must enter 1, 2 or 3.")

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("")

        print("You chose " +str(RPS(player)).replace('RPS.', '') + ".")
        print("Python chose " +str(RPS(computer)).replace('RPS.', '') + ".")

        print("")

        if player ==1 and computer ==3:
            print("🎉You Win!")
        elif player == 2 and computer ==1:
            print("🎉You Win!")
        elif player == 3 and computer ==2:
            print("🎉You Win!")
        elif player == computer:
            print("😯Tie game!")
        else:
            print("🐉Python wins!")

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n") 
            if playagain.lower() not in ["y","q"]:


                if playagain.lower() == "y":
                    return play_rps
                else:
                    print("\n🎉🎉🎉")
                    print("Thankyou for playing!\n")
                    sys.exit("Bye! 👋👋")

    

play_rps()

'''
    
En ter...
1 for Rock,
2 for Paper, or
3 for Scissors:

1

You chose Rock.
Python chose Paper.

🐉Python wins!

Play again?
Y for Yes or
 Q to quit

q

🎉🎉🎉
Thankyou for playing!

Bye! 👋👋

'''





