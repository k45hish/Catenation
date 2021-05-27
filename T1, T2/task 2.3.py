a=100
b=20
c=30
avg = (a+b+c)/2
print('avg = ', avg)
if avg>b and avg>b and avg>c:
    print('avg is higher than a,b,c')
elif avg>a and avg>b:
    print('avg is higher than a,b')
elif avg>a and avg>c:
    print('avg is higher than a,c')
elif avg>b and avg>c:
    print('avg is higher than b,c')
elif avg>a:
    print('avg is higher than a')
elif avg>b:
    print('avg is higher and b')
elif avg>c:
    print('avg is higher and c')
else:
    print('avg is too low')

