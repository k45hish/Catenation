print('Enter correct username and password combo to continue')
x=0
username = input('Enter username : ')
if username =='kashish':
    while x<3:
        password = input('Enter password: ')
        if password=='pass': 
            print('Access granted')
            break
        elif password !='pass' and x<2:
            print('Password is incorrect. Re-Type Password.')
            x += 1
            print('try number ',x+1)
        elif x==3:
            print('Password is incorrect. Access denied.')
            break
        else:
            print("Password is incorrect. Access denied.")
            break
elif username !='kashish':
    print("Username is incorrect. Access denied.")
