#1. Classes in Python
#Class is a blueprint of the real-life entity. In Python, it is created using the class keyword as shown in the following code snippet.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


'''In the above:
#class = Here is a class named Person.
Constructors have the default name __init__. They are functions that are implicitly called when an object of the class is created.
All instance methods including the constructor have their first parameter as self.
self refers to instance that is being referenced while calling the method.
name and age are the instance variables.'''

#2. Objects in Python
#Once a Person class is defined you can use it to create an instance by passing values as shown below.

if __name__ == "__main__":
    p = Person("ranjeeta", 23)
    print(p.name)
    print(p.age)

#In the above:
#p = is the name of the object that we are creating based on Person class
#Even though the "class" has three parameters "(self, name, age)", we’ll still "pass" only name and age while creating an object, as we don’t need to refer "self" here. It’s implicit.
#Once an object is created, you can refer to the attributes of the object using a dot. For example, "p.name" refers to the name attribute of that particular object
