"""
Functions:

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

"""
Creating a Function

In Python a function is defined using the def keyword:
"""
print("Creating a Function")
def my_function():
	print("my first function.")



"""
Calling a Function

To call a function, use the function name followed by parenthesis:
"""

my_function()



"""
Parameters

Information can be passed to functions as parameter.

Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, 
just separate them with a comma.

The following example has a function with one parameter (fname). When the function is called, we pass along a first name, 
which is used inside the function to print the full name:
"""
print("Function with Parameters")

def funct_with_parameter(fname):

	print("My first name is " + fname)


funct_with_parameter('john')



"""
Default Parameter Value

The following example shows how to use a default parameter value.

If we call the function without parameter, it uses the default value:
"""
print("Default Parameters Value")

def funct_with_default_parameters(fname, age=10):

	print("My name is " + fname + ". I'm " + str(age) + ' year old.')


funct_with_default_parameters('john', 24)
funct_with_default_parameters('john', 56)
funct_with_default_parameters('john')


"""
Passing a List as a Parameter

You can send any data types of parameter to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.

E.g. if you send a List as a parameter, it will still be a List when it reaches the function:
"""
print("Passing a List as a Parameters:")


def funct_with_paramets_as_list(list_parameter):

	for x in list_parameter:
		print(x)


a = ['apple', 'banana', 'orange']

funct_with_paramets_as_list(a)


"""
Return Values

To let a function return a value, use the return statement:
"""
print("Return Values:")


def funct_with_return(n):

	return n * 5


print(funct_with_return(5))
print(funct_with_return(10))
print(funct_with_return(456))





