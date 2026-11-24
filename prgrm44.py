import time
import datetime

now = datetime.datetime.now()

print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current week:", now.isocalendar()[1])
print("Weekday:", now.weekday())
print("Day of the year:", now.timetuple().tm_yday)
print("Day of the week:", now.strftime("%A"))
