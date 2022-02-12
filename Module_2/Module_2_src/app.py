# Import datetime librarie
from datetime import *
from dateutil.relativedelta import *

# Get the date and time info by using the now() function
now = datetime.now()
print(now)

# To the current datetime add (increase) one month, one week and 10 hours.
now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)
