import time
from datetime import datetime
import calendar

# Basic time lib
now = time.time()
print(now)
print(time.localtime(now))
print(time.asctime(time.localtime(now)))

# Basic datetime lib
print(datetime.now())
print(datetime(2022, 10, 15))
print(datetime.now().strftime("%d-%m-%Y"))

# Basic calendar lib
print(calendar.isleap(2022))
print(calendar.monthcalendar(2022, 10))
print(calendar.weekday(2022, 10, 15))
