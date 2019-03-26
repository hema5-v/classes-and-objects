#using init func in classes and objects-2
class Test:
	h=0
	def __init__ (self):
		self.h=8

	def myfunc(self,k):
		print("hi,i am in class")
		self.h=k
		print(self.h)

o=Test()
print(o.h)
o1=Test()	
print(o1.h)
o.myfunc(4)
o1.myfunc(2)
o3=Test()
print(o3.h)