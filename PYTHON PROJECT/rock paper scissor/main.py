import random

userWin = 0
computerWin = 0

option = ["rock","scissor","paper"]

while True:
    userChoice = input("Enter Rock/Paper/Scissor or type Q to quit: ").lower()
    if userChoice == "q":
        break
    if userChoice not in option:
        continue
    randomNumber = random.randint(0,3)
    computerChoice = option[randomNumber]
    print("computer choose ",computerChoice,".")
    if userChoice =="rock" and computerChoice == "scissor":
        print("you Won!")
        userWin +=1   
    elif userChoice =="paper" and computerChoice == "rock":
        print("you Won!")
        userWin +=1
    elif userChoice =="scissor" and computerChoice == "paper":
        print("you Won!")
        userWin +=1
    elif userChoice == computerChoice:
        print("It's a Tie!")
    else:
        print("You Lost!")
        computerWin +=1


print("You have won",userWin, "times")
print("Computer have won",computerWin, "times")
print("GoodBye!")