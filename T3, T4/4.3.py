def unique(l):
    lset = set(l)
    ulist =list(lset)
    return ulist

l1 = [1,2,33,4,5,6,7,7,8,9,9,9]
print("Original list :", l1)
print("Unique list : ", unique(l1))