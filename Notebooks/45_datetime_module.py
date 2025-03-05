import datetime

my_time = datetime.time(13,20,1,20)

print(my_time)
print(my_time.hour)
print(my_time.minute)
print(type(my_time))

print("-------------------------")
today = datetime.date.today()

print(today)
print(today.month)


print("-------------------------")
from datetime import datetime

my_datetime = datetime(2021,10,3,14,20,1)
print(my_datetime)
my_datetime = my_datetime.replace(year=2023)
print(my_datetime)

print("-------------------------")
# Date
from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
print(result)
print(type(result))
print(result.days)

print("-------------------------")
# Datetime
date_time_1 = datetime(2021,11,3,22,0)
date_time_2 = datetime(2020,11,3,12,0)

result = date_time_1 - date_time_2
print(result)