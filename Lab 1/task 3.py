password = input('Enter password: ')
numbers = '1234567890'
if len(password) < 16:
    print("Password is too short!")
elif password.isalpha() or password.isdigit():
    print("Bad password!")
else:
    print('Good password! You')

