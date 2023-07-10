#thực hành viêt và gửi dữ liệu thôgn qua code
import smtplib
import getpass
#caài đặt dữ liệu đăng nhâp cân thiêtý
t= 'pycharm450@gmail.com'
#cho ngươi dùngg nhâp ml
mk = getpass.getpass('pass: ')
send = 'hoduytruong280220@gmail.com'
#thưc hiện kết nói
bien =  smtplib.SMTP('smtp.gmail.com.',587)
#toạ lớp bao mật cho tk
bien.starttls()
#thực hiện đăng nhâp vào tìa khoản
bien.login(t,mk)
# thực hiện gửi tin nhắn
bien.sendmail(t,send,msg='day la tin nhan tu dong tu truong ')
print('sent mail')