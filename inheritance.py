'''3. Inheritance in Python
As the name suggest, this concept is about inheriting properties from an existing entity. This increases reusability of code. Single, Multiple and Multi-level inheritances are few of the many types supported by Python.

The following example shows how to use inheritance in python:'''


class Person:
  def __init__(self):
    pass

# Single level inheritance
class Employee(Person):
  def __init__(self):
    pass

# Multi-level inheritance
class Manager(Employee):
  def __init__(self):
    pass

# Multiple Inheritance
class Enterprenaur(Person, Employee):
  def __init__(self):
    pass

#In multiple inheritance, classes are inherited from left to right inside parenthesis, depending on Method Resolution Order (MRO) algorithm of Python
