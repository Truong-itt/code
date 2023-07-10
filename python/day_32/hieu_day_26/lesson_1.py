truong = [1,2,3]
#-> tao list
truong_moii = [n+1 for n in truong]
print(truong_moii)
#đói voi letter
truong_1 ='truong'
letter_split = [i for i in truong_1]
print(truong_1)
#dieu kien trong
bien  = ['truong','tuyen','khang','toi','thang']
ttt = [i for i in bien if len(i) <5]
print(ttt)
#noi dung can luu y là dạng dict trong kiểu như này
import random
truong_ttt = {ttt:random.randint(1,10) for ttt in bien}
print(truong_ttt)
tao_dieu_kien_dict = {hhh:score for (hhh,score) in truong_ttt.items() if score>5}
print(tao_dieu_kien_dict)
#bati tpa ten cong chieu dai ten
do_dai_dict = {bbb:len(bbb) for bbb in bien}
print(do_dai_dict)
print('van de dict row \n')
#hiểu về vân để truy cập khi gặp xử lí file pandas
student_dict = {
    'student':['truong','tuyen','thang','khang'],
    'score':[8,9,10,7]
}
#các dạng truy cạp dữ liêu khi gặp trường hợp này
for bien,giatri in student_dict.items():
    print(giatri)
print('van de khi truy cap file tuong tu như vậy  thông qua pandas\n\n')
import pandas
frame_new = pandas.DataFrame(student_dict)
print(frame_new)
print('cac huong truy cạp du lieu\n\n')
for bien,giatri in frame_new.iterrows():
    print(bien)
    print(giatri,'\n\n')
print('hướng dẫn truy cập thông qua chỉ mục của pandas \n\n')
for bien,giatri in frame_new.iterrows():
    print(giatri.student)
