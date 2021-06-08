l = []
for i in range(1,21):
    l.append(i)
x = filter(lambda x:x%2==0, l)
print(list(x))