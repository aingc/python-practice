# Strings in python are surrounded by either single/double quotation marks
name = 'Brad'
age = 37

# concatenation
print('Hello, my name is ' + name + ' and I am ' + str(age))

# str formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())
print(s.upper()) # all uppercase
print(s.lower()) # all lowercase
print(s.swapcase()) # swap case
print(len(s)) # get len of object: arr, str, lists, etc
print(s.replace('world', 'everyone')) # take world, replace with everyone
sub = 'h' # substr
print(s.count(sub)) # count number of 'h' in substring
print(s.startswith('hello'))
print(s.endswith('d'))
print(s.split()) # split words into list
print(s.find('r')) # find index of 'r'
print(s.isalnum()) # bool for if all alphanumberic
print(s.isalpha()) # bool for if all alphabetic
print(s.isnumeric()) # bool for if all numeric