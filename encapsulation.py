#4.Encapsulation

'''It is the concept of wrapping data such that the outer world has access only to exposed properties.
Some properties can be hidden to reduce vulnerability. 
This is an implementation of data hiding. 
For example, you want buy a pair of trousers from an online site. 
The data that you want is its cost and availability. 
The number of items present and their location is information that you are not bothered about. Hence it is hidden.

In Python this is implemented by creating private, protected and public instance variables and methods.

Private properties have double underscore (__) in the start, while protected properties 
have single underscore (_). By default, all other variable and methods are public.

Private properties are accessible from within the class only and are not available for child class(if inherited). 
Protected properties are accessible from within the class but are available to child class as well.
All these restrictions are removed for public properties.

The following code snippets is an example of this concept:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def _protected_method(self):
        print("protected method")
    def __private_method(self):
        print("privated method")

if __name__ == "__main__":
    p = Person("mohan", 23)
    p._protected_method() # shows a warning
    p.__private_method()  # throws Attribute error saying no such method exists