"""
Python Lamba:

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression

Syntax:

lambda arguments : expression

"""

print("Example 1: lambda")

x = lambda a : a + 10

print(x(5))



## Lambda functions can take any number of arguments:
print("Example 1: lambda multiple arguments")

y = lambda a, b: a + b

print(y(5, 30))


# A lambda function that sums argument a, b, and c and print the result:
print("Example 3: sum using lambda")

z = lambda a, b, c: a + b + c
print(z(35, 64, 64))


"""
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

print("Example 5: lambda with functions")


def my_funct(n):

	return lambda a: a * n


my_mul_of_2 = my_funct(2)
my_mul_of_3 = my_funct(3)

print(my_mul_of_2(2))
print(my_mul_of_3(3))





