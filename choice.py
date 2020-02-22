filename='user.txt'
name=input('Enter name: ')
passwd=input('Enter passcode: ')    
user = {'name':name,'password':passwd}

with open(filename,'a')as dat:
    for i,j in exec str((1,user)):
        dat.write(str([i,j]))
