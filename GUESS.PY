
secret_number = 2936
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess= int(input("Guess: "))
    guess_count +=1

    if guess == secret_number:
        print("Yeey! you won!")
        break
    else:
        print("sorry ...guess not correct!")
else:
    print("sorry you failed!")

