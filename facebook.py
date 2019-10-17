username= "kas"

password= "asd"

def login():
	
#getting user credentials
	user = input("Enter username:")
	passw  = input("Enter your password:")
#validating user credentials
	new_Validate(user, passw)


def new_Validate(user, passs):

	#print(password)
	#print(passs)
	if user == username and (passs==password):
		
		print("Welcome aboard! 💃️")
	else:
		print("Sorry! wrong credentials😅️")



def Validate(user, passs):
	if user == username :
		if passs== password:
			
			print("Welcome"+user )
		else:
			print("Wrong password")
	else:
		print("Invalid username..try again!")

login()
