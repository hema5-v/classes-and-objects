#using init func in classes and objects -1
class Test:
	rollno = 0
	def myfunc(self):
		print("hii,i am member of this func")
	def roll(self,k):
		self.rollno=k
		print("hii,im ",self.rollno)
	def __init__ (self,g):
		self.rollno=g
O=Test(101)
O.roll(305)
O1=Test(104)	
O1.roll(840)	
		