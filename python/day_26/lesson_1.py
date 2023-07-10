bien = [1, 2, 3]
bien2 = [i+1 for i in bien]
print(bien2)
bien3=[]
for i in bien:
    bien_nho = i+1
    bien3.append(bien_nho)
print(bien3)
ten ='truongdeptrai'
ten_moi=[]
# for i in ten:
#     bien_nho = i+1
#     ten_moi.append(bien_nho)
# print(ten_moi)
ten_moi=[i for i in ten]
print(ten_moi)
range_list = [i*2 for i in range(1,5)]
print(range_list)

names = ['truong','tuyen','khang','hue','hong']
#khi có điểu kiện
short_name = [i for i in names if len(i)<=5]
print(short_name)
long_name = [i.title() for i in names if len(i)>5]
print(long_name)