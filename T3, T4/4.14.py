svalue = int(input("Enter starting value for range : " ))
evalue = int(input("Enter ending value for range : " ))
evalue +=1
x= filter(lambda i: i%3!=0 and i%7==0, range(svalue,evalue))
print(list(x))