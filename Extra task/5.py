x = str(input('enter string : '))
print(x)
y = x[::-1]
print(y)
a = ""
for i in y:
    print(i)
    if i in "aeiouAEIOU":
        a += i
print(a)