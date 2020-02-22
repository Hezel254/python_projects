#this first code just explains how to create instances in classes

#class Dog:
#    species = 'mammal'
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#philo = Dog("philo",5)
#mikey = Dog("mikey",6)
#
#print("{} is {} and {} is {}.".format(philo.name,philo.age, mikey.name,mikey.age))
##is philo a mammal?
#if philo.species == "mammal":
#    print("{0} is a {1}!".format(philo.name, philo.species))

#PART 2

#second part helps one to create several instances and also see which cat is oldest

class Cat:
    species = "mammal" #class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
bruno = Cat("bruno",7)
jasmin = Cat("jasmin",3)
puffy = Cat("puffy",2)

#determine the oldest cat
def get_biggest_number(*args):
    return max(args)
#output
    print("The oldest cat is{} years old".format(get_biggest_number(bruno.age,jasmin.age,puffy.age)))

#PART 3

#class Dog():
#    species = "mammal"
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        #instance method
#    def description(self):
#        return"{} is {} years old".format(self.name, self.age)
#        #instance method
#    def speak(self,sound):
#        return "{} says {}".format(self.name, sound)
#    #instantiating the dog object
#    philo = Dog("philo",5) 
#    #call the instance method
#    print(philo.description())
#    print(philo.speak("Gruff Gruff"))
#        
    

#class Dog():
#    def __init__(self, breed):
#        self.breed = breed
#    def breed_name(self):
#        spencer = Dog("German Shepard") 
#        spencer.breed_name     
#        print(self.breed_name)
#         
#Dog
       
