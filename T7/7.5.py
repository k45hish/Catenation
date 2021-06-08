class Person():
    def __init__(self,age):
        if age<0:
           print ("Age is not valid, setting age to 0.")
           self.age = 0
        else:
            self.age = age
    def amIOld(self):
        if self.age<13:
           print ("You are young.")
        elif(self.age>=13 and self.age<=19):
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def YearPasses(self,yp):
        self.age+=yp
        print(self.age)


l = [-1,4,10,16,18,64,38]      
for x in l:
    a=Person(x)
    a.amIOld()
    print("")
a.YearPasses(4)