"""
Creating Variables

Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it
"""

print("Example 1:")

x = 5 
y = "John"
print(x)
print(y)


"""
Variables do not need to be declared with any particular type and can even change type after they have been set.
"""
print("Example 2:")

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

"""
String variables can be declared either by using single or double quotes:
"""
print("Example 3:")

x = "John"
# is the same as
x = 'John'
print(x)

"""
Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)

"""

"""
Assign Value to Multiple Variables

Python allows you to assign values to multiple variables in one line:
"""
print("Example 4:")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


"""
And you can assign the same value to multiple variables in one line:
"""
print("Example 5:")

x = y = z = "Orange"
print(x)
print(y)
print(z)

"""
Output Variables

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:
"""
print("Example 6:")

x = "awesome"
print("Python is " + x)


"""
You can also use the + character to add a variable to another variable:
"""

print("Example 7:")

x = "Python is "
y = "awesome"
z =  x + y
print(z)

"""
For numbers, the + character works as a mathematical operator:
"""
print("Example 8:")

x = 5
y = 10
print(x + y)

"""
If you try to combine a string and a number, Python will give you an error:
"""
print("Python will give you an error:")

x = 5
y = "John"
print(x + y)
