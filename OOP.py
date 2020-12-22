#object orientated programming in Python
#objects will have attributes and behaviours

#class = the design/blueprint to create the object 
#object = what the class produces

#define class:
class Computer:
	#behaviour (methods)
	def config(self):#this is the method
		print("i5, 16gb, 1TB")


#create necessary parameters/define parameter to call the function
com1 = Computer()
#pass the parameters to call the function 
Computer.config(com1)


com2 = Computer()
Computer.config(com2)

#alternative easier syntax
com1.config()
com2.config()


#this example is an int object, a(object) = 5(integer class), therefore a object type is an int
#a = 5
#print(type(a))#this will print what type of class it is 


#for each class you have to say what it equals so it knows if it is aafunction,int,string,float,etc...
#the below example is a function



