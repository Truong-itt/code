import smtplib
#sử dụng thộc tính để kết nối đến máy chủ email
my_email = 'hoduytruong280220@gmail.com'
password = 'Truongthongthai745'
connection = smtplib.SMTP('smtp.gmail.com')
#thiết lập môt bước bảo mật
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs='truongho642@gmail.com',msg='truong la nguoi dep trai nhat the gioi')
connection.close()
