"""
Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""

"""
Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class:
"""

## Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:

	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)


p = Person('Vinodkumar', 'Kouthal')
p.printname()

"""
Create a Child Class

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
"""

## Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
	pass

## Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

## Now the Student class has the same properties and methods as the Person class.

x = Student('Vinodkumar', 'Kouthal')
x.printname()


"""
Add the __init__() Function

So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).
"""

## Note: The __init__() function is called automatically every time the class is being used to create a new object.

## When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

## Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

## To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
	def __init__(self, fname, lname, year):
		Person.__init__(self, fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Welcome " + self.firstname + " " + self.lastname + " to the class of " + str(self.graduationyear))


y = Student('Mike', 'Olsen', 2018)
y.welcome()



