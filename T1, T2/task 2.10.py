c = 1
while c<=5:
    print('Guess number ', c)
    c=c+1
    x=int(input('Enter a number : '))
    if x==29:
        print('correct guess')
        break
    else:
        print('try again')
        continue