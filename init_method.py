#object orientated programming in Python
#objects will have attributes and behaviours

#class = the design/blueprint to create the object 
#object = what the class produces

#define class:
class Computer:
	#initialize objects (constructor), in this case we are passing three arguments/paramters 
	def __init__(self,cpu,ram):
		#assign values to an object
		self.cpu = cpu
		self.ram = ram



	#behaviour (methods)
	def config(self):#this is the method
		print("Config is",self.cpu,self.ram)


#create necessary parameters/define parameter to call the function
com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

#calls functions
com1.config()
com2.config()






#this example is an int object, a(object) = 5(integer class), therefore a object type is an int
#a = 5
#print(type(a))#this will print what type of class it is 


#for each class you have to say what it equals so it knows if it is aafunction,int,string,float,etc...
#the below example is a function
