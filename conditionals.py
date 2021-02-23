from copy import deepcopy

x = 10
y = 50

# simple if
if x > y:
  print(f'{x} is greater than {y}')

# if/else
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{y} is greater than {x}')

# logical operators and, or, not
if x > 2 and x <= 10:
  print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')

# Membership operators (not, not in) - Used to test if a sequence is presented in an obj

numbers = [1,2,3,4,5]

if x in numbers:
  print(f'{x in numbers}: {x} is in list')

if x not in numbers:
  print(f'{x not in numbers}: {x} is not in list')

'''
identity operators (is, is not) - Compare objects, not if equal, but if are the same
obj, with same mem location, so has to be deep copy?
'''

# is
if x is y:
  print(f'{x is y}: {x} is {y}')

# is not
if x is not y:
  print(f'{x is not y}: {x} is not {y}')

person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# shallow copy, so this would mean person is person2 would return false
person2 = person.copy()
person3 = deepcopy(person)
person['age'] = 35

# person2 is shallow copy of person
if person is person2:
  print(f'{person is person2}: {person} is {person2}')
else:
  print(f'{person is not person2}: {person} is not {person2}')


if person['age'] == person3['age']:
  print(f'Person age: {person["age"]} is equal to person3 age: {person3["age"]}')

if not(person['age'] == person3['age']):
  print(f'Person age: {person["age"]} is not equal to person3 age: {person3["age"]}')