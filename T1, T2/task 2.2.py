print('Enter 1 for addition'+'\n'+'Enter 2 for subtraction'+'\n'+'Enter 3 for division'+'\n'+'Enter 4 for multiplication'+'\n'+'Enter 5 for average')
x = int(input('enter number for calculation: '))
if x==5:
    a=int(input('enter first number : '))
    b=int(input('enter second number : '))
    print('Average: ', (a+b)/2)
else:

    num1 = int(input('enter the first number : '))
    num2 = int(input('enter the second  number : '))
    if x==1:
        y = num1+num2
        print('Addition: ',y)
    if x==2:
       y = num1-num2
       print('Subtractoin: ',y)
    if x==3:
        y = num1/num2
        print('Division: ', y)
    if x==4:
        y = num1*num2
        print('Multiplication :', y)
