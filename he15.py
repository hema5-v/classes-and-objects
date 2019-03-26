#assigning valus to  object
class Test:
	rollno = 0
	def myfunc(self):
		print("hii,i am member of this func")
	def roll(self,k):
		self.rollno=k
		print("hii,im ",self.rollno)
O=Test()
O.roll(101)
O1=Test()	
O1.roll(104)	
