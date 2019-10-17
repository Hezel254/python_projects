Class DogMother (object):

	def__init__(self):
		self.ear_color='White'
		self.name= 'Jas'
		
Class DodFather (object):
	def__init__(self):
	self.leg_color='white'
	self.name='Bruno'
	
Class Puppy(DogMom,DodFather):
	''' A puppy is the child of the mother dog 	 	and the father dog'''
	
	def__init__(self):
		print("yeey! Puppy is born")
		self.ear_color= DogMom.ear_color
		
