#this is a sample code that enables the player to input a guess between 0-100,
#apparently only the owner of the code knows exactly what is the secret number 
#and the players are expected to guess random numbers for the game, the count of 
#the guesses will be incremented and the player will get the number of times he/she had guessed.

import random

minimum = 0
maximum = 100
number = random.randint(minimum, maximum)
try = 0
running = True
answer =  None

while running:
    print(" is it %s?" str(number))
    answer = raw_input()
    if "no" in answer.lower() and "higher " in answer.lower():
        number -= random.randint(1,5)
    
    elif "no" in answer .lower() and higher "in" answer.lower():
        number += random.randint (1,5)

    elif answer.lower() == "no":
        print("Higher or lower?")

        answer= raw_input()

        if answer.lower() == "higher":
            number += random.randint (1, 5)

        elif answer.lower() == "lower":
            number -= random.randint(1,5)
    elif  answer.lower == "yes":
        if try < 2:
            print("yes it took me only %s try!" %str (try))
        elif try < 2 and >10:
            print(" pretty well for a robot, %s tries ." %str (try))

        else:
            print(" that's so bad, %s tries!" %str(try ))


    running = False

    try += 1

    print(" kudos...thanks for playing")             




