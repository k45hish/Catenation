l = []

for i in range(1,11):
    l.append(i)
a= filter(lambda x:x%2==0, l)
num=list(a)
b=map(lambda x:x*x, num)
print(list(b))