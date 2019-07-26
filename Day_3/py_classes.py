"""
Python Classes/Objects

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

"""
Create a Class

To create a class, use the keyword class:
"""
class Myclass:
	x = 5


"""
Create Object

Now we can use the class named myClass to create objects:
"""
p1 = Myclass()
print(p1.x)


"""
The __init__() Function

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do 
when the object is being created:
"""


class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age


p = Person("john", 28)
print(p.name)
print(p.age)


# Note: The __init__() function is called automatically every time the class is being used to create a new object


"""
Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
"""

class Human:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def my_funct(self):
		print("Hello my name is " + self.name)


h = Human('john', 23)
h.my_funct()

## Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"""
The self Parameter

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:
"""

class Person1:

	def __init__(myself, name, age):
		myself.name = name
		myself.age = age

	def my_funct(person):
		print("Hello, my name is " + person.name)

pp = Person1('vinod', 23)
pp.my_funct()

# Modify Object Properties


# Delete Object Properties


# Delete Objects





