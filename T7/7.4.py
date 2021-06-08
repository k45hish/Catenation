class Time():
	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime(t1,t2):
		hr=t1.hours+t2.hours
		mn =t1.mins+t2.mins
		temp=(hr*60)+mn
		t3=Time(0,0)
		while temp>=60:
			temp-=60
			t3.hours+=1
		t3.mins=temp
		return t3

	def displayTime(self):
		print("The time is", self.hours,"hours and", self.mins, "minutes.")

	def displayMinute(self):
		print ("The total time in minutes is :", (self.hours*60) + self.mins)

x = Time(3,30)
y = Time(4,15)
z = Time.addTime(x,y)
z.displayTime()
z.displayMinute()

