import math
inp = input("Enter the comma-separated sequence number : ")
inpl = inp.split(',')
print("value of comma-separated sequence D :", inpl)
x = []
for d in inpl:
    q = round(math.sqrt(2 * 50 * eval(d) / 30),2)
    x.append(q)
print(x)