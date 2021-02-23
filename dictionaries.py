# Dictionary - unordered collected, changeable, indexed. No Duplicate. Key Value pairs

# Create dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

print(person, type(person))

# Dictionary constructor
# person2 = dict(firstname='Sara', last_name='Williams')

# print(person2, type(person2))

# Get value
# person.first_name won't work
print(person['first_name']) # more common way
print(person.get('last_name'))

# Add key/val
person['phone'] = '555-555-5555'

print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict, SHALLOW COPY
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)
print(person)

# Remove item
del(person['age']) # Deletes the single value
person.pop('phone') # Retursn removed value

# Clear
person.clear()

# Get length
print(len(person2))
print(person)

# List of dict
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])