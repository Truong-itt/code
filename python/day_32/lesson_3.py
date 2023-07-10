#bai tap su dungj pandass vaf thu bien datetim va cahs guiwr mail
#goi thu vieenj
import datetime as dt
import random
import getpass
import smtplib
 #laay sra ngayf hien tai
now = dt.datetime.now()
#kieerm tra xem cos phari la thu hai neu la thu hai thi gui tin nhan chuc ngay moi tu file
weekday = now.weekday()
# print(weekday)
#thoong tin dan nnap
t = 'pycharm450@gmail.com'
# cho ngươi dùngg nhâp ml
mk = getpass.getpass('pass: ')
send = 'hoduytruong280220@gmail.com'
if weekday == 5:
    #doc file
    with open('quotes.txt') as file:
        #docj duw liwu file
        contents = file.readlines()
        queue = random.choice(contents)
    print(queue)
    #su dung phuont thuc with dde ket noi va gui file di
    with smtplib.SMTP('smtp.gmail.com.', 587) as bien:
        # toạ lớp bao mật cho tk
        bien.starttls()
        # thực hiện đăng nhâp vào tìa khoản
        bien.login(t, mk)
        # thực hiện gửi tin nhắn
        bien.sendmail(t, send, msg=f"Subject:Monday positive\n\n{queue}")
        print('sent mail')