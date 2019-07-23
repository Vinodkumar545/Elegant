"""
Set

A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
"""

print("Create a Set:")

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Access Items

You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
by using the in keyword.
"""
print("Loop through the set")

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


print("Check if 'banana' is present in the set:")

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


"""
Change Items

Once a set is created, you cannot change its items, but you can add new items.
"""
print("Once a set is created, you cannot change its items, but you can add new items.")

"""
Add Items

To add one item to a set use the add() method.

To add more than one item to a set use the update() method.
"""
print("add() fn:")

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


print("update() fn:")
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

"""
Get the Length of a Set

To determine how many items a set has, use the len() method.
"""
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


"""
Remove Item

To remove an item in a set, use the remove(), or the discard() method.
"""
print("remove() fn")
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print("If the item to remove does not exist, remove() will raise an error.")

print("discard() fn:")

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

print("If the item to remove does not exist, discard() will NOT raise an error.")

"""
You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

"""
x = thisset.pop()

print(x)

print(thisset)

# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

print("clear() fn:")

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


print("del keyword:")

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

"""
The set() Constructor

It is also possible to use the set() constructor to make a set.
"""
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


"""
Set Methods

Python has a set of built-in methods that you can use on sets.

Method									Description
add()							Adds an element to the set
clear()							Removes all the elements from the set
copy()							Returns a copy of the set
difference()					Returns a set containing the difference between two or more sets
difference_update()				Removes the items in this set that are also included in another, specified set
discard()						Remove the specified item
intersection()					Returns a set, that is the intersection of two other sets
intersection_update()			Removes the items in this set that are not present in other, specified set(s)
isdisjoint()					Returns whether two sets have a intersection or not
issubset()						Returns whether another set contains this set or not
issuperset()					Returns whether this set contains another set or not
pop()							Removes an element from the set
remove()						Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()							Return a set containing the union of sets
update()						Update the set with the union of this set and others


"""
