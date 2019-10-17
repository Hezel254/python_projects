users = {}


class Usser(object):
	def __init__(self, name, key):
		self.name = name
		self.friends=[]
		self.key= key
		self.is_offline= False
		self.is_online= False
	def login(self):
		print(f"{self.name} login activated!")

#validating user credentials 

	def validate(user, passs):
		if user==self.name and passs==self.key:
			if passs==password:
				print("Welcome"+ user)
				self.is_online = True
		else:
			print("Invalid username or password")
			
	def view_friends(self): 
		pass
	
	def register_users():
		this_username = input("Enter username :  ")
		this_password =input("Enter password :  ")
	
		this_user = Usser(this_username, this_password)
	
	#record this user to the dictionary
	
		users[this_username]= this_user
	
options= '''
1. Register
2. Login
3.View Friends
4. See all the users...
5. Exit

'''
while True:
	command = input(f'{options} select an option: ')
	if command is '5':
		print("Goodbye")
		break
	elif command is '1':
		register_users()
	elif command is '4':
		for user in users: print(user)
	else:
		print("Invalid option")


