print('Enter 1 for addition'+'\n'+'Enter 2 for subtraction'+'\n'+'Enter 3 for division'+'\n'+'Enter 4 for multiplication'+'\n'+'Enter 5 for average')
x = int(input('enter number for calculation: '))
if x==5:
    a=int(input('enter first number : '))
    b=int(input('enter second number : '))
    c=(a+b)/2
    if c<0:
        print('Negative')
    else:
        print('Average: ', c)
else:
    if x==1:
        num1 = int(input('enter the first number : '))
        num2 = int(input('enter the second  number : '))
        y = num1+num2
        if y<0:
            print('Negative')
        else:  
            print('Addition: ', y)
   
    elif x==2:
        num1 = int(input('enter the first number : '))
        num2 = int(input('enter the second  number : '))
        y = num1-num2
        if y<0:
            print('Negative')
        else:  
            print('Subtraction: ', y)
    
    elif x==3:
        num1 = int(input('enter the first number : '))
        num2 = int(input('enter the second  number : '))
        y = num1/num2
        if y<0:
            print('Negative')
        else:  
            print('Division: ', y)
    
    elif x==4:
        num1 = int(input('enter the first number : '))
        num2 = int(input('enter the second  number : '))
        y = num1*num2
        if y<0:
            print('Negative')
        else:  
            print('Multiplication: ', y)
    else:
        print('please give a valid input')
