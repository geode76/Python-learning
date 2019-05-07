# This program says hello and asks for my name.

print('What is your name?')  #ask for their name
myName = input()
if myName == 'Alice':
    print('Enter your password Alice')
    password = input()
    if password == 'ABC123':
        print('Access granted')
    else:
        print('Invalid password')
else:
     print('No access')