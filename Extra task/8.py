even_list = []
odd_list = []
c = 0
while c<5:
    c += 1
    x=int(input("Enter a number between 1 and 50 :"))
    
    if x%2==0 and x<=50:
        print("Valid number.")
        even_list.append(x)
    elif x%2!=0 and x<=50:
        print("Valid number.")
        odd_list.append(x)
    else:
        print("this is not a valid number.")
        c -= 1

print("Even list:",even_list,",\n Sum of even list :",sum(even_list), ",\n Max of even list", max(even_list))
print("Odd list",odd_list, ",\nSum of odd list :", sum(odd_list), ",\n Max of odd lsit", max(odd_list))