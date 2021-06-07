x=1
while x>0 or x<0 or x==0:
    x = int(input('guess the lucky number : '))

    if x==29:
        print("correct number entered")
        break
    
    else:
        print('incorrect number entered')
        answer = str(input('do you want to continue?: '))
    if answer=='yes':
        continue
    else:
        break