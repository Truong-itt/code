import pandas as pd
import smtplib
import random
from datetime import datetime
import getpass
#sử dụng truy cập dữ liệu bằng comprehensive
t= 'pycharm450@gmail.com'
#cho ngươi dùngg nhâp ml
mk = getpass.getpass('pass: ')
send = 'hoduytruong280220@gmail.com'
#thực hiện dộc file từ file csv
data = pd.read_csv('birthdays.csv')
print(data)
#sử dụng thư viêện truy cập vao ngày hiện tại
now = datetime.now()
print(now)
#thực hiện gán ngày sinh nhật vao ngay hôm nay trong đoạn code trên
today_tuple = (now.month,now.day)
print(today_tuple)
#thưchj hiện trích suât lây dữ liệu tử file có sản
#mcụ tiêu tạo thành một cái dict để nap dữ liệu vào
#yêu cầu nhớ vững kiến thức dữ liệu cũ
#xac định lây dữ liệu tử một nguồn index là hai cột và giá trị sẽ tự vao
#diêm đặc biệt khi ta truy cập vao kiểu dữ liẹu kiẻu này
birthdays_dict = {(bien["month"],bien["day"]):bien for bien,bien in data.iterrows()}
print(birthdays_dict)
#tiến hành chúc mừng sinh nhật baby truong
if today_tuple in birthdays_dict:
    #có 3 file chúc mưungf tôi sẽ lấy đại ra một trong 3 fild đẻ xử lsí

    file_path =  f"letter_{random.randint(1,3)}.txt"
    #toạ biên tổng truy cập bao dữ liệu có trước trong khung dữ liêu j
    birthdays_person  = birthdays_dict[today_tuple]
    #mở fiel và lấy nối dụng cần lây ra
    with open(file_path) as file:
        contens = file.read()
        #thay đỏi dữ liệu cần thay đỏi trong file
        #truy cập bào cột name để lấy tên ra khỏi dữ liệu
        contens = contens.replace("[NAME]",birthdays_person ['name'])
    #thực hiện gửi file đi
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        #tiến hành login vào tài khoản cần đăng nhập
        connection.starttls()
        connection.login(t,mk)
        connection.sendmail(t, send, msg=f"Subject:Happy Birthday!\n\n{contens}")
        print('sent mail')
