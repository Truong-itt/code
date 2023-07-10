student_dict = {
    'student':['truong','tuyen','khang'],
    'diem':[9,8,7]
}
# for (key,value) in student_dict.items():
#     print(value)
import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# loop through a data frame(lăp qua một khung dữ liệu)
# for (key,value) in student_data_frame.items():
    # print(value)
    # print(key)
# in ra từng phân tử ở từng vị trí
for (key,row) in student_data_frame.iterrows():
    print(row)
    # print(key)
# for (key,row) in student_data_frame.iterrows():
#     print(row.student)
# for (key,row) in student_data_frame.iterrows():
#     print(row.diem)
# for (key,row) in student_data_frame.iterrows():
#     if row.student == 'truong':
#         print(f'diem cua truong la:{row.diem}')