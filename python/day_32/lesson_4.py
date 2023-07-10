import pandas as pd
import smtplib
import random
from datetime import datetime

sender_email = 'pycharm450@gmail.com'
sender_password ='zneshxkyixfhjkul'


# Lấy thông tin email người nhận và thông tin sinh nhật
receiver_email = 'hoduytruong280220@gmail.com'
today = datetime.now()
today_tuple = (today.month, today.day)

# Đọc dữ liệu từ file CSV và lưu vào dictionary
data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Kiểm tra xem có người nào có sinh nhật hôm nay hay không
if today_tuple in birthdays_dict:
    # Lấy thông tin người có sinh nhật
    birthday_person = birthdays_dict[today_tuple]
    # Đọc nội dung email từ file ngẫu nhiên
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        # Thay thế tên người nhận trong nội dung email
        contents = contents.replace("[NAME]", birthday_person['name'])
    # Thực hiện kết nối đến SMTP server của Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        # Gửi email
        connection.sendmail(sender_email, receiver_email, msg=f"Subject:Happy Birthday!\n\n{contents}")
        print('Sent email')
else:
    print('No birthdays today')