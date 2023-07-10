# import smtplib
# import getpass
# my_email = 'pycharm450@gmail.com'
# password = getpass.getpass('pass: ')
# #gửi cho ai
# email_send = 'hoduytruong280220@gmail.com'
# email_send = 'hoduytruong280220@gmail.com'
# #xử lí dữ liệu
# with smtplib.SMTP('smtp.gmail.com',587) as session:
#     #trỏ tới startlist có chức năng enable bảo mật cho gmai
#     session.starttls()
#     session.login(my_email,password)
#     #nôi dụng gưi là gì thì phải chỉ rõ
#     email_content = '''
#     Subject:hello
#     day la truong gui cho truong o hien tai
#     '''
#     session.sendmail(my_email
#                      ,email_send
#                       ,email_content)
#     print('mail sent')


#thưc hành lấy ra ngyà giời hiện tại bằng python
import datetime as dt
bien = dt.datetime.now()
day_of_week = bien.weekday()
month = bien.month
year = bien.year
print(bien)
print(day_of_week)
#lưu dữ liệu ngày sinh nhật tron bộ đếm python
date_of_brith = dt.datetime(year=2000,month=12,day=15)
print(date_of_brith)

#thực hiện việc gửi email thông qu việc trích xuất file hiện có
#cụ thể ở đây là tô igủi cho tôi
#thực hiện yêu cầu trong file main

