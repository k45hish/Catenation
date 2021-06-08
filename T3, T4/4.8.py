def sqnum(x,y):
    l=[]
    for i in range(x,y+1):
        a = i*i
        l.append(a)
    t=tuple(l)
    print(t)

(b,c)=(1,20)
sqnum(b,c)