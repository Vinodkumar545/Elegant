"""
Python Lamba:

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression

Syntax:

lambda arguments : expression

"""

print("Example 1: lambda")

x = lambda a: a + 10
print(x(5))


## Lambda functions can take any number of arguments:
print("Example 1: lambda multiple arguments")
z = lambda a, b: a + b
print(z(5, 7))


# A lambda function that sums argument a, b, and c and print the result:
print("Example 3: sum using lambda")
s = lambda a, b, c: a + b + c
print(s(12, 3, 5))


"""
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

print("Example 5: lambda with functions")
def my_funct(n):
	return lambda a: a * n

mydoubler = my_funct(5)
print(mydoubler(5))



