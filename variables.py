# single line comment

'''
Multiline comment/docstring (used to define a function's purpose)
can be single or double quotes
'''

"""
  Vars must start with a letter or an underscore
  - Can have numbers, but not start with one
"""

# x = 1           # cast as int as default
# y = 2.5         # float
# name = 'john'   # str
# is_cool = True  # bool

# multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# basic addition
a = x + y

print('Hello')
print(x, y, name, is_cool, a)

# check type
print(type(x))

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(x), type(y), y, type(z), z)