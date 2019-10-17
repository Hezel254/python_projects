class Mammal:
	def walk(self):
		print("walk")




class Dog(Mammal):
	pass


class Cat(Mammal):
	pass

dog1= Dog()
dog1.walk()

print(type(dog1))

print(dog1.walk())
