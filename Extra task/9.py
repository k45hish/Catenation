x = "12abcbacbaba344ab"
a={}
for i in x:
    if i.isalpha():
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    else:
        pass
for y, z in a.items():
    print(y,"=",z)