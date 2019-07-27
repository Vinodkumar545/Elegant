"""
Python Conditions and If statements

Python supports the usual logical conditions from mathematics:

	Equals: a == b
	Not Equals: a != b
	Less than: a < b
	Less than or equal to: a <= b
	Greater than: a > b
	Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

print("Example 1: If statement:")




"""
Explaination:

In this example we use two variables, a and b, which are used as part of the if statement 
to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, 
and so we print to screen that "b is greater than a".
"""

"""
Indentation

Python relies on indentation, using whitespace, to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
"""
print("Example 2: Indentation")




"""
Elif

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
"""

print("Example 3: Elif")





"""
Explaination:

In this example a is equal to b, so the first condition is not true, but the elif condition is true, 
so we print to screen that "a and b are equal".
"""

"""
Else

The else keyword catches anything which isn't caught by the preceding conditions.
"""

print("Example 4: Else")




"""
Explaination:

In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
"""

# You can also have an else without the elif:

print("Example 5: Else without elif")



"""
Short Hand If

If you have only one statement to execute, you can put it on the same line as the if statement.
"""

# One line if statement:
print("Example 5: Short Hand if")


"""
Short Hand If ... Else

If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
"""

# One line if else statement:
print("Example 6: Short Hand If ... Else")



# You can also have multiple else statements on the same line:
print("Example 7: multiple else statements on the same line:")


"""
And

The and keyword is a logical operator, and is used to combine conditional statements:
"""
print("Example 8: And")


"""
Or

The or keyword is a logical operator, and is used to combine conditional statements:
"""
print("Example 9: Or")





