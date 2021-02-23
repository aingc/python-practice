# python doesn't use curly braces for functions, just indentations with tabs or spaces


# Create function
def sayHello(name='Sam'):
  print(f'Hello {name}')

sayHello('John Doe')
sayHello()

# Return vals
# def getSum(num1, num2):
#   return num1+num2

# num = getSum(3, 4)
# print(num)

# lambda func is a small anon func
# can take any num of args, but can only have one expression. Similar to JS arrow funcs

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))