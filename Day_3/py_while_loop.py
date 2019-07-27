"""
Python Loops

Python has two primitive loop commands:

	1. while loops
	2. for loops

"""

"""
The while Loop

With the while loop we can execute a set of statements as long as a condition is true.
"""
print("Example: While loop")
i = 1
while i < 6:
	print(i)
	i = i + 1



"""
Note:

The while loop requires relevant variables to be ready, 
in this example we need to define an indexing variable, i, which we set to 1.

** remember to increment i, or else the loop will continue forever.
"""

"""
The break Statement

With the break statement we can stop the loop even if the while condition is true:
"""
print("Example 2: Break Statement")

i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i = i + 1




"""
The continue Statement

With the continue statement we can stop the current iteration, and continue with the next:
"""
print("Example 3: continue Statement")

i = 1
while i < 6:
	
	i += 1
	if i == 3:
		# print(i)
		continue

	print(i)
	
	







