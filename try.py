secret_number=7
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    guess= int(input("guess: "))
    guess+=1

    if guess==secret_number:
        print("you won!")
        break
else:
    print("sorry you failed!")

