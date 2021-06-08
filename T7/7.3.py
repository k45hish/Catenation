def three_numbers(nums):
    n = sorted(nums)
    l = len(n)
    a = []
    nset = False
    for i in range(0, l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if (n[i] + n[j] + n[k] == 0):
                    a.append([n[1],n[j],n[k]])
                    nset = True
    print(a)
    if (nset == False):
        print("There is no set of three-element, whose sum equal to zero.")
 

n = [-25, -10, -7, -3, 2, 4, 8, 10]
three_numbers(n)
