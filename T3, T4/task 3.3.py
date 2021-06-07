def multiplyList(myList) :
	result = 1
	for x in myList:
		result = result * x
	return result

def addList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + addList(list, size - 1)
	
list1 = [2,2,3]
print('Multiplication: ', multiplyList(list1))

total = addList(list1, len(list1))
print("Addition: ", total)
