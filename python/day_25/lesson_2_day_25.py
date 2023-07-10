import pandas
#bước 1 đọc file
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_Squirrel_Data.csv')
print(data)

#truy cập vào Primary Fur Color có màu gray
#tính so luong cua loài sóc này
grey = data[data['Primary Fur Color'] == 'Gray']
grey_len = len(data[data['Primary Fur Color'] == 'Gray'])

print(grey_len)

#tuong tu thi tim den con mau Cinnamon và Black
red_len = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_len = len(data[data['Primary Fur Color'] == 'Black'])
print(red_len)
print(black_len)

#hoc cach áp dụng datframe vao trong file
data_dict = {
    'fur color':['Gray','Cinnamon','Black'],
    'count':[grey_len,red_len,black_len]
}
data_convert_frame = pandas.DataFrame(data_dict)
#tao thanh mot file csv moi bang pandas
data_convert_frame.to_csv('so_luong_mau_soc.csv')
print(data_convert_frame)