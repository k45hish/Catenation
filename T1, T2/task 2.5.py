l = list(range(2000,3200))
k = []
for x in l:
    if x%7==0 and x%5!=0:
        k.append(x)
print(k)