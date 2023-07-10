import smtplib
import datetime as dt
import random
'''
gmail_my = 'pycharm450@gmail.com'
mk ='zneshxkyixfhjkul'
send_to = 'hoduytruong280220@gmail.com'

now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)
if weekday == 1:
    #-> lay du lieu gui tin nhan
    with open('quotes.txt') as bien:
        contens = bien.readlines()
        quote = random.choice(contens)
    # print(quote)
    #lay duoc tin nhan thi gui di
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(gmail_my,mk)
        connection.sendmail(gmail_my,send_to,msg=f"subject:monday motivative\n\n{quote}")
    print('mail sent')
'''

from datetime import datetime
import pandas

now = dt.datetime.now()
today_tuple = (now.month,now.day)
# print(today_tuple)
data = pandas.read_csv('birthdays.csv')
# print(data)
gmail_my = 'pycharm450@gmail.com'
mk ='zneshxkyixfhjkul'
send_to = 'hoduytruong280220@gmail.com'


birthday = {(giatri['month'],giatri['day']):giatri for bien,giatri in data.iterrows()}
# print(birthday)

#xu li khi va cham voi ngay sinh nhat
if today_tuple in birthday:
    #xac dinh vao the nào trong file mà lay giá tri
    birthday_person = birthday[today_tuple]
    file_path = f'letter_{random.randint(1,3)}.txt'
    with open(file_path) as file:
        contens = file.read()
        contens.replace("[NAME]",birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(gmail_my,mk)
        connection.sendmail(gmail_my,send_to,
                            msg=f"Subject:Happy Birthday!\n\n{contens}")
    print('sent mail')