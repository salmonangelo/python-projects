print("welcome to my quiz game!")

def  quit():
    print("bye! catch up later")
 
permission = input("are willing to start the game? : ")

if permission.lower() != "yes" :
    quit()

print("Let's play :)")
score = 0

question = input("What is the capital of India?")
if question.lower() == "new delhi":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("How many continents are there in the world?")
if question.lower() == "seven":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("What is the boiling point of water?( in celesius)")
if question.lower() == "100c":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("WWho wrote the play Romeo and Juliet?")
if question.lower() == "william shakespeare":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("What is the largest planet in our solar system?")
if question.lower() == "jupiter":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("Which animal is known as the 'King of the Jungle'?")
if question.lower() == "lion":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("How many sides does a triangle have?")
if question.lower() == "three":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("What is the name of our galaxy?")
if question.lower() == "milky way":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("Who was the first Prime Minister of India?")
if question.lower() == "jawaharlal nehru":
   print("Correct!")
   score += 1
else:
   print("Wrong!")

question = input("Which organ in the human body pumps blood?")
if question.lower() == "heart":
   print("Correct!")
   score += 1
else:
   print("Wrong!")



print("your score is " + str(score))
print("you got "+ str((score/10)*100)+ "%")












