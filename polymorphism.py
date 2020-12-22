#5. Polymorphism in Python
#This is a concept where a function can take multiple forms depending on the number of arguments or type of arguments given to the function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_salary(self):
        print("Salary is unknown")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def show_salary(self):
        print("Salary is", self.salary)

if __name__ == "__main__":
    p = Person("y", 23)
    x = Employee("x", 20, 100000)
    p.show_salary() # Salary is unknown
    x.show_salary() # Salary is 100000


'''In the above example, super keyword is used to call a method of parent class. 
Both classes have the method show_salary. 
Depending on the object type that makes a call to this function, the output varies.'''

#Python has inbuilt-polymorphism functions as well. One of the simplest examples is the print function in python. E.G. Below:

print("Hello there", end=" ")
print("I am TEST1")
print(len([1, 2, 3, 4, 5]))

#The output of this code will be:
'''Hello there I am TEST1
	5'''

'''In the above code snippet:

The end keyword parameter changed the functionality of print function. Hence it did not end ‘Hello There’ with an end-line.
len([1, 2, 3, 4, 5]) in third line return an int. The print recognizes the data type and implicitly converts it to string and prints it to the console'''