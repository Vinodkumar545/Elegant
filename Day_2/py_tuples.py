"""
Tuple

A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
"""

print("create tuple")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Access Tuple Items

You can access tuple items by referring to the index number, inside square brackets:
"""

print("Access Tuple Items")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""
Change Tuple Values

Once a tuple is created, you cannot change its values. Tuples are unchangeable.
"""
print("Once a tuple is created, you cannot change its values. Tuples are unchangeable.")

"""
Loop Through a Tuple
You can loop through the tuple items by using a for loop.
"""
print("Loop Through a Tuple")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
	print(x)

"""
Check if Item Exists

To determine if a specified item is present in a tuple use the in keyword:
"""
print("Check if Item Exists")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
	print("Yes, 'apple' is in the fruits tuple")


"""
Tuple Length

To determine how many items a tuple has, use the len() method:
"""

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


"""
Add Items

Once a tuple is created, you cannot add items to it. Tuples are unchangeable
"""
print("Once a tuple is created, you cannot add items to it. Tuples are unchangeable")

print("ERROR")

thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

"""
Remove Items

Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
"""

print("Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:")

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

"""
The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple.
"""
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


"""
Tuple Methods

Python has two built-in methods that you can use on tuples.

Method					Description
count()		Returns the number of times a specified value occurs in a tuple
index()		Searches the tuple for a specified value and returns the position of where it was found

"""






