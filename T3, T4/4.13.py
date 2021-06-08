from functools import reduce
x = reduce(lambda s,i: s+str(i),[1,2,3,4,5,6,7],'')
print(x)