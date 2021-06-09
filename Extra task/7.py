def getsum(x, sum):
    n = len(x)
    temp = []
    for i in x:
        for j in x[(i-1):]:
            if x[i] + x[j] == sum:
                y = (x[i],x[j])
                temp.append(y)
            if i==(n-2) and j==(n-1):
                break
    print(temp)
    
x = [1,2,3,4,5,6,7,8,9,-1]
sum = 8
getsum(x, sum)