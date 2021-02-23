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

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

print(today, timestamp)

# pip3 install, installs globally, like npm install -g
# pip3 freeze, will show all modules installed, in this case, it's in a global scope