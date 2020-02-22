""" A simple scrpt to validate user input"""
passs='home'
user='hezzy'

def try_again():
    ass=input('Try again y/n:>>>')
    if ass=='y':
        get_user()


def get_user():
    username=input('Enter username: ')
    pasword=input('Enter pasword: ')
    if username==user and pasword==passs:
        print('Welcome aboard! 💃️')
    if username==user and pasword!=passs:
        print('sorry {},wrong pasword'.format(username))
        try_again()
    elif username!=user and pasword==passs:
        print('Wrong username')
        try_again()
    else:
        if username!=user and pasword!=passs:
            print('Invalid credentials!!,you gonna be reported 😅️')
            try_again()

if __name__ == "__main__":
    get_user()