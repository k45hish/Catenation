c = 1
while c<=5:
    print('Guess number ', c)
    c=c+1
    x=int(input('Enter a number : '))
    if x==29:
        print('correct guess')
        break
    if c==6:
        print('Sorry but that was not very successful')
        break

    if x!=29:
        print('try again')
        continue