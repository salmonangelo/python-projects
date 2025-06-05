import random

def roll():
    minValue = 1
    maxValue = 6
    roll = random.randint(minValue,maxValue)
    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            break
    else:
        print("Enter a valid number!")

maxScore = 50
noOfPlayers = [0 for _ in range(players)]

while max(noOfPlayers) < maxScore:
    
    for idx in range(players):
        print("\nPlayer number", idx+1 ,"turn has started!")
        print("your current score is",noOfPlayers[idx],"\n")
        currentValue =0

        while True:
            shouldRoll = input("would you like to roll(y): ")
            if shouldRoll.lower() != "y":
               break

            value = roll()
            if value == 1:
                print("you rolled 1! Your done!")
                currentValue = 0
                break
            print("you have rolled",value,"!")
            currentValue += value
            print("your current score is", currentValue)
        noOfPlayers[idx] += currentValue

        

    

maxScore = max(noOfPlayers)
winnerIndex = noOfPlayers.index(maxScore)
print("The winner is player naumber",winnerIndex+1, "and his score is",maxScore)