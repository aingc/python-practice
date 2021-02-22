# List - an ordered collection and changeable. Can have duplicates

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

# Get a val
print(fruits[1])

# get len
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into pos
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

fruits.reverse()

# Sort alphabetically
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)
print(fruits)