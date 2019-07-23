"""
String Literals

String literals in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""

print("Hello")
print('Hello')


a = "Hello"
print(a)

"""
Multiline Strings

You can assign a multiline string to a variable by using three quotes:
"""

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


"""
Or three single quotes:
"""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


"""
Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1. 
Square brackets can be used to access elements of the string.

"""

a = "Hello, World!"
print(a[1])

b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))


# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))


# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


"""
String Format

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))




