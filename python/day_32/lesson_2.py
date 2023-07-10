#hiểu vè viêcj truy cập thời gian
import datetime as dt

#lấy ra ngày luc nay
now = dt.datetime.now()
#từ ngay lấy ra năm thang ngay
#uuwy y dang nay chi có ngay thu may trong tuan mơi duoc chuyen du lieu dau ()
month = now.month
year = now.year
day_of_week = now.weekday()
print(day_of_week)

#tạo ra một ngay với dữ liệu cô sđinh
bien  = dt.datetime(year=2000,month=10,day=23,hour=4)
print(bien)