f = open("C:/Users/kmava/Desktop/Catenation/T5, T6/doc.txt","r")
x = f.readline()
for x in f:
    if len(x)%2==0:
        print(x)
    else:
        pass

