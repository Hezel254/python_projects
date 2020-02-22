# Guess the number game
import random
guess_taken=0
name = input("heyo, what is your name? ")
print("Well " + name +  ", I'm thinking of a number between 1 and 30")
secret_number = random.randint(1,30)

for i in range(3):
    guess_taken+=1
    guess = int(input("take a guess:"))

    if guess < secret_number:
        print("guess is too low")
    elif guess > secret_number:
        print("guess is too high")
    else:
        break

if guess == secret_number:
    print("Yeey", name, "you guessed my number in", guess_taken,'guesses')
else:
    print("Nope, actually the number i was thinking of was", secret_number)


