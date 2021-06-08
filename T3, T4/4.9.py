def showNumbers(x):
    for i in range(x+1):
        if i%2==0:
            print(i, "EVEN")
        elif i%2!=0:
            print(i, "ODD")
limit = int(input("Enter your limit for even-odd number :"))
showNumbers(limit)
