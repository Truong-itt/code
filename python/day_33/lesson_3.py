import requests
import smtplib
import time
import getpass
from datetime import datetime
#thưu hiện dưu xliệu cho việc gửui mail
t= 'pycharm450@gmail.com'
mk = getpass.getpass('pass: ')
send = 'hoduytruong280220@gmail.com'
#truyên dữu liệu co hàm requests
my_lat = 10.651161
my_lng = 106.617925
#viet hàm ktra dữ liệu của iss có dang ở trên vung mình bay qua hay không
def is_iss_overhead():
    #sử dung jphươung thức kết nối vưới hệ thống iss
    response = requests.get("http://api.open-notify.org/iss-now.json")
    #kểm tra đã dược kết nói chưa
    response.raise_for_status()
    # lây dử liệu của iss
    data = response.json()
    #truy cập vào kinh độ vĩ đọ hiện tại của iss
    #truy cập vao kinh độ và vĩ đọ của dữ liệu nhận được
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    #thưuc hiện theo tác kiểm tra
    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True
def is_night():
    #truyên dữu liệu vào iss để biết là bây giừo có phải là ban đêm hay không
    #gom nhóm đẻ truyên co dữ liệu
    parameters={
        'lat':my_lat,
        'lng':my_lng,
        'formatted':0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400",params=parameters)
    #tương ụt kiểm tra dữ liệu có bị lỗi không
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

     #truy cập để biết dữ liệu lây ra có đugns là buổi tôi hay không
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    #thưuc hiện ktra dữ liệu dựa trên hai hàm được viết săn
    if is_iss_overhead and is_night:
        #kêt nối với gmail và thông báo về việc iss đang bay rtên đầu mình
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(t,mk)
        connection.sendmail(t,send,msg="Subject:Look Up\n\nThe iss above you in the sky")
        print("sent mail")
        break