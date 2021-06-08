
def selfmultiply (l):
    a = l*l
    return a
user_list=[1,2,3,4,5,6,7,8,9,10,11,12]
x=map(selfmultiply, user_list)
print(type(x))
print(list(x))
 
