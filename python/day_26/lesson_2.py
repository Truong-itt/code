#chương trình random điểm số cho sinh vien
import random
names=['truong','tuyen','hoa','hieu','nghia']
list_score = {i:random.randint(1,10) for i in names}
print(list_score)
passed_student = {i:diem for (i,diem) in list_score.items() if diem >= 5}
print(passed_student)