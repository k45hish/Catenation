l=[22,69,6,68,56,55,99,59,84,85]
print("original list : ", l)

for i in l:
    if(i%2 == 0):
        l.remove(i)

print("Odd numbers list : ", l)