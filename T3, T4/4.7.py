
def length(str1,str2):
    if len(str1)==len(str2):
        print(str1)
        print(str2)
    elif len(str1)>len(str2):
        print(str1)
    else:
        print(str2)

x = input("Enter string 1 :")
y = input("Enter string 2 :")

length(x,y)