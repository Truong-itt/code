##################### Extra Hard Starting Project ######################
#ca đặt thư viện để chạy đoạn code
import smtplib
import pandas
from datetime import datetime
import getpass
today =datetime.now()
today_tuple = (today.month,today.day)
# 1. Update the birthdays.csv
print(today_tuple)
print(type(today_tuple))
# 2. Check if today matches a birthday in the birthdays.csv
#đọc dữ liệu khung tử file pandas trong lập trình python
data = pandas.read_csv('birthdays.csv')
print(data)
#chuyển đổi dữ liệu xem thửu
# data_row = ('name':)
# bitthdays_dict = {(data_row['month'],data_row['day'])}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




