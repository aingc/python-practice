people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person in people:
#   print(f'Current Person: {person}')

# Break
# for person in people:
#   if person == 'Sara':
#     break
#   print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range
# for i in range(len(people)):
#   print(people[i])

# for i in range(0, 11):
#   print(f'Number: {i}')

# While loop
count = 0
while count <= 10:
  print(f'Count: {count}')
  count += 1

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('fizzbuzz')

  if i % 3 == 0:
    print('fizz')
  elif i % 5 == 0:
    print('buzz')
  else:
    print(i)