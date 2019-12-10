import json
filename = "user.json"

def new_user():
   username = input("Provide username: ")
   with open(filename,'w')as dat:
       json.dump(username,dat)
       return username

def stored_username():
    try:
        with open(filename)as dat:
            username = json.load(dat)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = stored_username()
    if username:
        print("Welcome back {}".format(username))
    else:
        username = new_user()
        print("We'll remember you next time {}".format(username))


greet_user()

