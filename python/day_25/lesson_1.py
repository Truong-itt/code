#lấy dữ liệu
import pandas
data = pandas.read_csv('weather_data.csv')
print(data['temp'])
print(type(data['temp']))
#chuyển dữ liệu thành từ điển
data_dict = data.to_dict()
print(data_dict,"\n")
#chuyển dữ liệu thành kiểu list của cột temp(nhiệt độ)
temp_list = data['temp'].to_list()
print(len(temp_list))
#truy câp vao tính trung  bình
tb = sum(temp_list) / len(temp_list)
print(f'nhiet do tb trong danh sach {tb}')
#tính trung bình nhanh bang ham có san
print(data['temp'].mean())
#co mot cach giup truy cap nhanh vao
print(data.condition)


#truy cap vao hang thay vi cot
bien = data[data.day == 'Monday']
print(bien)
#tuong tu truy cap vao phan tu co nhiet do cao nhat
bien_nhiet_max = data[data.temp == data.temp.max()]
print(bien_nhiet_max)
#truy cap vao dúng phân tưu can co
monday = data[data.day == 'Monday']
montday_temp =  int(monday.temp)
convert = montday_temp * 9/5 +32
print(f'nhiet do sau khi chuyen doi la {convert}')