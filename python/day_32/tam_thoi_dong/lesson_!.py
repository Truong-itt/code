import datetime as dt
#xác đinh thời gian
now = dt.datetime.now()
year = now.year
month = now.month
#xác đinh ngày trong tuần
day_of_week = now.weekday()
print(day_of_week)
date_of_birth = dt.datetime(year = 1995,month=12,day=15,hour=4)
print(date_of_birth)