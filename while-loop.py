password = ''
while password != 'python123':
    password = input('enter your password')
    if password == 'python123':
        print('you are logged in')
    else:
        print('wrong password')