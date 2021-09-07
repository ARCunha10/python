import random
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

youRock = "You have selected Rock!"
computerRock = "Computer has selected Rock!"
youPaper = "You have selected Paper!"
computerPaper = "Computer has selected Paper!"
youScissors = "You have selected Scissors!"
computerScissors = "Computer has selected Scissors!"
youWon = Fore.WHITE + Back.GREEN + "You won!"
computerWon = Fore.WHITE + Back.RED + "Computer won!"
tie = Fore.WHITE + Back.BLUE + "It is a Tie!"

wins = 0
losses = 0
ties = 0

print(Fore.WHITE + Back.BLUE + "Lets Play ROCK, PAPER, SCISSORS")

yourChoice = input(
    Fore.WHITE
    + Back.BLUE
    + "Enter your move: [r]ock, [p]aper, [s]cissors or [q]uit"
    + " "
    + Style.RESET_ALL
)

while yourChoice in yourChoice:

    words = ("r", "p", "s")
    words = random.choice(words)

    # you chose rock
    if yourChoice == "r" and words == "r":
        print(youRock)
        print(computerRock)
        print("Rock versus Rock...")
        print(tie)
        ties = ties + 1
    elif yourChoice == "r" and words == "p":
        print(youRock)
        print(computerPaper)
        print("Rock versus Paper...")
        print(computerWon)
        losses = losses + 1
    elif yourChoice == "r" and words == "s":
        print(youRock)
        print(computerScissors)
        print("Rock versus Scissors...")
        print(youWon)
        wins = wins + 1
    # you chose paper
    elif yourChoice == "p" and words == "r":
        print(youPaper)
        print(computerRock)
        print("Paper versus Rock...")
        print(youWon)
        wins = wins + 1
    elif yourChoice == "p" and words == "p":
        print(youPaper)
        print(computerPaper)
        print("Paper versus Paper...")
        print(tie)
        ties = ties + 1
    elif yourChoice == "p" and words == "s":
        print(youPaper)
        print(computerScissors)
        print("Paper versus Scissors...")
        print(computerWon)
        losses = losses + 1
    # you chose scissors
    elif yourChoice == "s" and words == "r":
        print(youScissors)
        print(computerRock)
        print("Scissors versus Rock...")
        print(computerWon)
        losses = losses + 1
    elif yourChoice == "s" and words == "p":
        print(youScissors)
        print(computerPaper)
        print("Scissors versus Paper...")
        print(youWon)
        wins = wins + 1
    elif yourChoice == "s" and words == "s":
        print(youScissors)
        print(computerScissors)
        print("Scissors versus Scissors...")
        print(tie)
        ties = ties + 1
    # you chose exit
    elif yourChoice == "q":
        print(Fore.WHITE + Back.BLUE + "Thank you for playing!")
        sys.exit()
    # unknown option
    elif yourChoice != words or "q":
        print()
        print(Fore.WHITE + Back.RED + "Unknown Option Selected!")

    print()
    print(
        f"{Fore.WHITE + Back.GREEN} {wins} Wins {Style.RESET_ALL} {Fore.WHITE + Back.RED} {losses} Losses {Style.RESET_ALL} {Fore.WHITE + Back.BLUE} {ties} Ties "
    )
    print()
    yourChoice = input(
        Fore.WHITE
        + Back.BLUE
        + "Enter your move: [r]ock, [p]aper, [s]cissors or [q]uit"
        + " "
        + Style.RESET_ALL
    )
