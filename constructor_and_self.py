
class Computer:
	def __init__(self):
		self.name = "Test"
		self.age = 28

#Computer() is the constructor
c1 = Computer()
c2 = Computer()
#prints address in heap memory of "c1"
print(c1.name)
print(c1.age)