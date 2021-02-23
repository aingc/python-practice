# Tuple - ordered collection, unchangeable, can have duplicates

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# tuple constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# if one value in tuple, you want trailing comma so as to be of type: tuple
fruits2 = ('Apples',)
print(fruits, fruits2)
print(fruits2, type(fruits2), type(fruits))

# get value of tuple
print(fruits[1])

# cannot change value
# fruits[0] = 'Pears'
# delete tuple
del fruits2
# print(fruits2) ... will not longer be defined

print(len(fruits))

# Set - unordered collection, unindexed, no duplicates

# Create set
fruits_set = {'Apples', 'Orange', 'Mango'}

# Check if in set
print('Apples' in fruits_set) # returns bool

# Add to set
fruits_set.add('Grape')

print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set entirely, DIFFERENT ENTIRELY FROM DELETING
fruits_set.clear()

print(fruits_set)

del fruits_set
print(fruits_set) # errors as fruits_set isn't defined after being deleted

# When trying to add a duplicate, there won't be an error, it just won't add the duplicate
fruits_set.add('Apples')