# Python has funcs for CRUD with files

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed) # check if closed within script
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('Python')
myFile.write(' and JavaScript')
myFile.close()

# still want to append to file
myFile = open('myfile.txt', 'a') # a for append, we don't want to overwrite with w
myFile.write(' also React')
myFile.close()

print('Is Closed: ', myFile.closed) # check if closed within script

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100) # read 100 chars
print(text)