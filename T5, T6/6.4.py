def reverse(str):
    length = len(str)
    for i in range(length-1, -1, -1):
        yield str[i]

for x in reverse('Consultadd Training'):
    print(x)