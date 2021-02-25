import time

username = 'subash'
password = 'password'
username_input = input('username: ')
password_input = input('password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('loading')
    time.sleep(1)
    print('...')
    print('ALright you passed the security measures and passed the test')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')
