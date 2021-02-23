'''
For creating objects, a class is like a blueprint. An obj has props and methods.
Almost everything in Python is an obj
'''

# Create class
class User:
  # Constructor - a func that runs when you instantiate an obj from a class
  # self is like 'this'
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
    
  def has_birthday(self):
    self.age += 1

# Extend class
# similar to 'extends User' from something like Java
class Customer(User):
  # Constructor
  def __init__(self, name, email, age, balance=0):
    self.name = name
    self.email = email
    self.age = age
    self.balance = balance

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user obj
corey = User('Corey Aing', 'c@gmail.com', 555)
# Initi customer obj
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

print(type(corey))
print(corey.age)
corey.has_birthday()
print(corey.greeting())