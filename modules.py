'''
A module is a file containing a set of funcs to include in an application.
There are core python modules, modules you can install using pip pkg manager
(including Django) as well as custom modules
'''
# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is invalid')

print(today, timestamp)

# pip3 install, installs globally, like npm install -g
# pip3 freeze, will show all modules installed, in this case, it's in a global scope