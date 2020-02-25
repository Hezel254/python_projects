#load the username, if it has already been previously stored
#if not, prompt the username and store it

import csv
FILENAME = "username.csv"
#try:
#with open (filename)as data:
#except file not found errors:
def addUser(username, password):
    with open(FILENAME,'a',newline = " ") as f:
        writer = csv.writer(f)
        writer.writerow(username, password)
def retrieveUsers():
    with open(FILENAME,'a',newline = '') as f:
        usernames = csv.reader(f)
        return usernames
def login():
    option = int(input("Enter 0 for sign up and 1 for sign in: "))
    if option == 0:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        addUser(username, password)
        return "welcome aboard!"
    elif option == 1:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        users = retrieveUsers()
        for user in users:
            if user[0] == username and user[1] == password:
                return True
            return False
print(login())
    
        
   
    

        
#    print("Welcome aboard!")
#
#
#def login():
#    #getting the user credentials
#    username =input('Enter your name: ')
#    password =input("password should be alphabets and numbers\nEnter password: ")
#    #validating the user credentials
#    #new_validate (user,passs)
#    #def new_validate(user, password):
#        #if user == username and passs == password:
#            #print("Welcome Aboard")
#       # else:
#          #  print("Wrong credentials")
#   # def validate (user, password):
#         
#
#    if username == 'ann' and password == 1234:
#      
#        print("Welcome Aboard" + user)
#     
#login()
##using random.seed() and random.sample() together
#import random
#Meals_list = ['Tea','Coffee','Bread','Eggs', 'Pudding cup']
#random.seed(2)
#sample_list = random.sample(Meals_list,2)
#
#print(random.sample(sample_list,2))
#
#random.seed(3)
#sample_list = random.sample(Meals_list,2)
#print(sample_list)