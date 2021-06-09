x = (1,2,3,4,5,6,7,8,9,10)
xlist = list(x)
even = []
for i in xlist:
    if i%2==0:
        even.append(i)
    else:
        pass
a = tuple(even)
print(a)
