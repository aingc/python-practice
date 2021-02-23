'''
A module is a file containing a set of funcs to include in an application.
There are core python modules, modules you can install using pip pkg manager
(including Django) as well as custom modules
'''
# a core python module: datetime
import datetime
from datetime import date
import time
from time import time

# today = datetime.date.today()
today = date.today()
timestamp = time()

print(today, timestamp)