

a=2
b=3
print(a)


a='Hello'
b="Hello"
c="""Python is a PL
it is easy to learn"""
print('a','b','c')



s1='Hello world'
s2=s1.replace('world','python')
print(s2)




list_list=[ ['apple','mango','orange'],[123,345,567]]
for x in list_list:
	print(x)

"""for list_index in range(len(list_list)):
	print(list_list[list_index])"""

print(type(list_list))
for x in list_list:
	print(type(x))
	for y in x:
		print(y)





tuple1=('apple','mango','orange')
print(type(tuple1))

print(tuple1[0])
print(tuple1[1])

for x in tuple1:
	print(x)


for x_index in range(len(tuple1)):
	print(tuple1[x_index])

print(len(tuple1))





