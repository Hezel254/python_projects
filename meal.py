username='hez'
password=1234

def log():
    user=input('Enter name: ')
    pass_=int(input('Enter password: '))
    if user==username and pass_==password:
        print('Welcome')
    else:
        print('Access Denied')
log()