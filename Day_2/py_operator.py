"""
Python Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

	1. Arithmetic operators
	2. Assignment operators
	3. Comparison operators
	4. Logical operators
	5. Identity operators
	6. Membership operators
	7. Bitwise operators
"""

"""
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator		Name		   Example
	+		Addition			x + y	
	-		Subtraction			x - y	
	*		Multiplication		x * y	
	/		Division			x / y	
	%		Modulus				x % y	
	**		Exponentiation		x ** y	
	//		Floor division		x // y	
"""
print("Arthematic Operators: ")
x = 5
y = 3

print(x + y)

"""

Python Assignment Operators

Assignment operators are used to assign values to variables:

Operator    Example		Same As
	=		x = 5		x = 5	
	+=		x += 3		x = x + 3	
	-=		x -= 3		x = x - 3	
	*=		x *= 3		x = x * 3	
	/=		x /= 3		x = x / 3	
	%=		x %= 3		x = x % 3	
	//=		x //= 3		x = x // 3	
	**=		x **= 3		x = x ** 3	
	&=		x &= 3		x = x & 3	
	|=		x |= 3		x = x | 3	
	^=		x ^= 3		x = x ^ 3	
	>>=		x >>= 3		x = x >> 3	
	<<=		x <<= 3		x = x << 3

"""
print("Assignment Operators")
x = 5

x += 3

print(x)

"""

Python Comparison Operators

Comparison operators are used to compare two values

Operator	  Name						Example
	==		Equal						x == y	
	!=		Not equal					x != y	
	>		Greater than				x > y	
	<		Less than					x < y	
	>=		Greater than or equal to	x >= y	
	<=		Less than or equal to		x <= y

"""
print("Comparison Operators:")

x = 5
y = 3

print(x == y) # returns False because 5 is not equal to 3

"""

Python Logical Operators

Logical operators are used to combine conditional statements:

Operator			Description												Example
	and 	Returns True if both statements are true					x < 5 and  x < 10	
	or		Returns True if one of the statements is true				x < 5 or x < 4	
	not		Reverse the result, returns False if the result is true		not(x < 5 and x < 10)

"""
print("Logical Operators:")

x = 5

print(x > 3 and x < 10) # returns True because 5 is greater than 3 AND 5 is less than 10

"""

Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator				Description										Example
is 			Returns true if both variables are the same object			x is y	
is not		Returns true if both variables are not the same object		x is not y

"""
print("Identity Operators:")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

"""
Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

Operator				Description																Example
in 			Returns True if a sequence with the specified value is present in the object		x in y	
not in		Returns True if a sequence with the specified value is not present in the object	x not in y

"""
print("Membership Operators:")

x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

"""

Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:


Operator	Name					Description
	& 		AND				Sets each bit to 1 if both bits are 1
	|		OR				Sets each bit to 1 if one of two bits is 1
 	^		XOR				Sets each bit to 1 if only one of two bits is 1
	~ 		NOT				Inverts all the bits
	<<		Zero fill 		Shift left by pushing zeros in from the right and let the leftmost bits fall off
			left shift
	>>		Signed right 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
			shift
"""




