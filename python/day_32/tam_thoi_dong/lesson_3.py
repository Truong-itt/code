#hiểu về việc gửi gmail tbăng thư viện trong lập trình pỵthon
import smtplib
#tránh bị lộ thôgng tin băng việc acc thêm thư viện getpass
import getpass
my_email = 'pycharm450@gmail.com'
password = getpass.getpass('pass: ')
#gửi cho ai
email_send = 'hoduytruong280220@gmail.com'
#xử lí dữ liệu
session = smtplib.SMTP('smtp.gmail.com',587)
#trỏ tới startlist có chức năng enable bảo mật cho gmai
session.starttls()
session.login(my_email,password)
#nôi dụng gưi là gì thì phải chỉ rõ
email_content = '''
Subject:hello
day la truong gui cho truong bang thu tu dong bang thu vien trong pycharm
'''
session.sendmail(my_email,email_send,email_content)
print('mail sent')

