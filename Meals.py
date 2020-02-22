#load the username, if it has already been previously stored
#if not, prompt the username and store it

import json
filename = "username.json"
#try:
#with open (filename)as data:
#except file not found errors:
username = input("Your name")
with open(filename,'a') as data:
    json.dump(username, data)
    print("Your data has already been uploaded")
else:
    print("Welcome aboard!")


def login():
    #getting the user credentials
    username =input('Enter your name: ')
    password =input("password should be alphabets and numbers\nEnter password: ")
    #validating the user credentials
    #new_validate (user,passs)
    #def new_validate(user, password):
        #if user == username and passs == password:
            #print("Welcome Aboard")
       # else:
          #  print("Wrong credentials")
   # def validate (user, password):
         

    if username == 'ann' and password == 1234:
      
        print("Welcome Aboard" + user)
     
login()
#using random.seed() and random.sample() together
import random
Meals_list = ['Tea','Coffee','Bread','Eggs', 'Pudding cup']
random.seed(2)
sample_list = random.sample(Meals_list,2)

print(random.sample(sample_list,2))

random.seed(3)
sample_list = random.sample(Meals_list,2)
print(sample_list)