"""
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

"""
print("create list:")

thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
Access Items

You access the list items by referring to the index number:
"""
print("Access Items")

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

"""
Change Item Value

To change the value of a specific item, refer to the index number:
"""
print("Change Item Value")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

"""
Loop Through a List

You can loop through the list items by using a for loop:
"""
print("Loop Through a List:")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
 	print(x)


"""
Check if Item Exists

To determine if a specified item is present in a list use the in keyword:
"""
print("check if item Exists:")

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


"""
List Length

To determine how many items a list has, use the len() method:
"""
print("List Length:")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Add Items

To add an item to the end of the list, use the append() method:
"""
print("Add Items:")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


print("Insert Items:")

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""
Remove Item

There are several methods to remove items from a list:
"""
print("Remove Item:")

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

## The pop() method removes the specified index, (or the last item if index is not specified):

print("pop Item:")

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


## The del keyword removes the specified index:

print("del Item:")

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

## The del keyword can also delete the list completely:
print("del list")

thislist = ["apple", "banana", "cherry"]
del thislist

## The clear() method empties the list:
print("clear list")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""
Copy a List

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

"""

# 1. Make a copy of a list with the copy() method:

print("1. copy list")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# 2. Another way to make a copy is to use the built-in method list()
print("2. built-in method:")

thislist = ["apple", "banana", "cherry"]

mylist = list(thislist)
print(mylist)


"""
The list() Constructor

It is also possible to use the list() constructor to make a new list
"""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
List Methods

Python has a set of built-in methods that you can use on lists.

Method				Description
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list

"""


