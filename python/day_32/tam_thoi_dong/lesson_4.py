import smtplib
import getpass
#thực hiện setup để đăng nhâp vào tk gmail
my_email = 'pycharm450@gmail.com'
password = getpass.getpass('pass: ')
#email ngươi nham
truong = 'hoduytruong280220@gmail.com'
#thiêt lập thư viện để đăng nhập vao tài toàn
bien = smtplib.SMTP('smtp.gmail.com',587)
bien.starttls()
bien.login(my_email,password)
#thiết lập gửi nội dung đi
email_content = '''
Subject:hello
day la truong gui cho truong bang thu tu dong bang thu vien trong pycharm
'''
bien.sendmail(my_email,truong,email_content)
print('mail sent')