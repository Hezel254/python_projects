import random
guess_taken = 0

print("Hey! what's your name?")
name = input()
print('So ' +name+ ' , i was thinking of a number between 1 and 20')
secret_number = random.randint(1,20)

for guess_taken in range (3):
    guess_taken +=1
    print('Take a guess')
    guess = int(input())

    if guess_taken < secret_number:
        print('Sorry, guess is too low')
    elif guess_taken > secret_number:
        print('Oops! guess is too high')
    else:
        break

if guess_taken == secret_number:
    print('Congratulations' +name+ ' , you guessed my number in'+ str(guess_taken) +" guesses")

else:
    print("Nop, the number i was thinking of was "+ str(secret_number))