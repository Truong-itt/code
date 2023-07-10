import random
import smtplib
import getpass
import pandas
import datetime as dt
my_email = 'pycharm450@gmail.com'
password = getpass.getpass('pass: ')
#gửi cho ai
email_send = 'hoduytruong280220@gmail.com'
#thực hiện lấy dữ liệu thòi gian
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    #tiến hành mở file nếu là thứ hai trong tuân
    with open('quotes.txt') as quote_file:
        content = quote_file.readlines()
        bien_2 = random.choices(content)
    print(bien_2)
    with smtplib.SMTP('smtp.gmail.com',587) as session:
        #trỏ tới startlist có chức năng enable bảo mật cho gmai
        session.starttls()
        session.login(my_email,password)
        #nôi dụng gưi là gì thì phải chỉ rõ
        email_content = bien_2
        session.sendmail(my_email
                         ,email_send
                          ,msg=f"Subject: Monday productive\n\n{bien_2}")
        print('mail sent')

# email_send = 'hoduytruong280220@gmail.com'
# #xử lí dữ liệu
