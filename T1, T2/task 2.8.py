y = input("Input a string : ")
n=l=0
for x in y:
    if x.isdigit():
        n=n+1
    elif x.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Numbers", n)