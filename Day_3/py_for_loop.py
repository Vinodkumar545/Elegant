"""
Python For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

print("Example 1: Looping Through a List")

# The for loop does not require an indexing variable to set beforehand.



"""
Looping Through a String

Even strings are iterable objects, they contain a sequence of characters:
"""
print("Example 2: Looping Through a String")



"""
The break Statement

With the break statement we can stop the loop before it has looped through all the items:
"""
print("Example 3: The Break Statement on List")

# Exit the loop when x is "banana":


# Exit the loop when x is "banana", but this time the break comes before the print:


"""
The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:
"""
print("Example 4: The Continue Statement")



"""
The range() Function

To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number.

The range() function defaults to 0 as a starting value, 
however it is possible to specify the starting value by adding a parameter: range(2, 6), 
which means values from 2 to 6 (but not including 6):

"""
print("Example 5: range() function")

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.



"""
The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
"""
print("Example 6: range() fn with increment")




"""
Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
"""
print("Example 7: Else in For Loop")



"""
Nested Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
"""









