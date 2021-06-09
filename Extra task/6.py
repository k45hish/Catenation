def even(x): 
    y = x.split(' ') 
    print(y)
    a = ""
    for z in y:
        if len(z)%2==0:
            a += " "+ z
        else:
            a = a
    return a  
x = "hello my name is abcde paresh kumar " 
y = even(x)
print (y.lstrip())