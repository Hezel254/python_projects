name = input('enter your name: ')
print('Welcome aboard ' + name  )
course = input('Enter your course: ')
list = []
marks = int(input("So,what number of marks would you want to enter " + name + " ?"))
for i in range(marks):
    n = int(input('Enter mark: '))
    list.append(n)
    total = sum(list)
    print('Total marks are: ', sum(list))
    avg = sum(list) / marks
print ('You have an average of', avg)



















