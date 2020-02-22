#grade system
name=input('Enter your name>>> ').title()
count=0
count1=int(input('How many units do have?>>>'))

active=True
num1=[]

while active:
    for i in range(count1):
        count+=1
        mark=int(input('Enter your marks>>>'))
        num1.append(mark)
        active=False
        average=sum(num1)/count1
    print(name,'you got',average,'as average')
    