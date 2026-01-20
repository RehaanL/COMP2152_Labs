#COMP 2154 Lab 02 - Rehaan Lachporia 101594859

#importing modules for functionality
import random, time

#defining starting array and variables
choices = ["Rock", "Paper", "Scissors"]
winCounter = 0
loseCounter = 0

#printing a welcome message for user
print("Welcome to the most epic game of Rock, Paper, Scissors you will ever play in your life!")
print("1 = Rock, 2 = Paper, 3 = Scissors\n")


def rpsGameLogic():
    playerChoice = int(input("Choose your weapon: "))

    if playerChoice < 1 or playerChoice > 3:
        print("Error: Choice must be between 1 and 3")
        print("1 = Rock, 2 = Paper, 3 = Scissors\n")
        #function recursion
        rpsGameLogic()
    elif playerChoice == 1 or 2 or 3:
        print("An interesting choice. Lets see how you fair\n")

    for _ in range(3):
        (print("!!!WARNING!!!", end="", flush=True), time.sleep(.5),
         print("", end="\r", flush=True), time.sleep(.5))

    print("A foe has appeared!\n"), time.sleep(1)

    print("Computer: I see... You have chosen well, but I will choose better"), time.sleep(1.3)
    print("Computer: Prepare to FIGHT!!!\n"), time.sleep(2)

    computerChoice = random.randint(1, 3)
    print("Your opponent has made their decision. Your fate now hangs in the balance!\n")

    #little "Loading" animation to build suspense
    for _ in range(3):
        print("Loading", end="", flush=True), time.sleep(0.5),
        print(".", end="", flush=True), time.sleep(0.5),
        print(".", end="", flush=True), time.sleep(0.5),
        print(".", end="", flush=True), time.sleep(0.5),
        print("", end="\r", flush=True)


    print("You chose:", choices[playerChoice-1]), time.sleep(.5)
    print("Computer chose:", choices[computerChoice-1]), time.sleep(.5)

    global winCounter
    global loseCounter
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
        winCounter += 1
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
        winCounter += 1
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
        winCounter += 1
    else:
        print("You lose!")
        loseCounter+= 1

    #Clasic Rock message
    if playerChoice != 1:
        print("You didn't pick the classic Rock...")

    #Printing the Win/Loss Counter
    print(f"Wins: {winCounter} Losses: {loseCounter}")

    restart = input("Would you like to play again? (Y/N): ")
    if restart == "Y" or "y'":
        #function recursion
        rpsGameLogic()
    else:
        print("Thanks for playing!"), time.sleep(2)
        exit()

rpsGameLogic()









