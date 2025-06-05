import random



while True:
    upperLimit = input("Type the range of number to guess: ")
    if upperLimit.isdigit():
        upperLimit = int(upperLimit)
        if upperLimit <= 0:
            print("enter a number great than zero!")
        else:
            break
    
    else:
        print("Omly numbers are allowed!")
   



randomNumber = random.randint(0,upperLimit)


guess = 0
while True:
    guess += 1
    actualGuess = int(input("guess the number: "))
    if actualGuess == randomNumber:
        print("You got it!")
        break
    elif actualGuess > randomNumber:
        print("your above the number!")
    elif actualGuess < randomNumber:
        print("your below the number!")


print("you find it in "+ str(guess)+ "th guess")
quit()
    
        
#something


