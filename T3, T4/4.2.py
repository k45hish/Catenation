x = "abcSdefPghijQkl"
def case(x):
    up = 0
    low = 0
    for i in x:
        if i >="a" and i <="z": low = low + 1
        elif i >="A" and i <="Z": up = up + 1
    print("Uppercase characters :", up, "Lowercase Characters : ", low)
case(x)