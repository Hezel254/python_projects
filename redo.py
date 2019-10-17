class Student():
    def __init__(self,name,age):
        self.self= self
        self.name= name
        self.age= age

#asking user for credentials
    def register_users(self):
        name = input("what is your name?")
        age = input("what is your age?")  
              
    def course_study(self):
        pass

    options= """
    1.Sign in
    2.Enter aggregate points.}
    3.Select campus of choice
    4.Register
    5.Submit
    6.Exit  """


    while True:
        command = input(f'{options}select an option: ')
        if command is '1':
            register_users(self)
        elif command is '3':
            print("Selection completed")
        elif command is '5':
            print("Submission successful!")
        elif command is  '6':
            print("Bye Bye")  
        else:
            print("Sorry! option not recognized...")      
        