"""
Python JSON

JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

"""

"""
Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the json.loads() method.
"""
import json

x = '{"name": "john", "age": 30, "city": "new york"}'

print(type(x)) # type str

y = json.loads(x)

print(type(y)) # type dict


"""
Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
"""

a = {
	'name': 'john',
	'age': 10,
	'city': 'new york'
}

print(type(a)) # type dict

y = json.dumps(x)

print(type(y)) # type str

# read the json file
with open('py_json.json', 'r') as rj:
	data = json.load(rj)

print(data)


# Write into JSON file

with open('py_write_json.json', 'w') as writefile:
	json.dump(a, writefile)


