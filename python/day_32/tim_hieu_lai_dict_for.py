import random
import pandas as pd
t=['truong','tuyen','khang','hau','trung','nghia']
#toạ dict moi tu t
b= {bien:random.randint(1,10) for bien in t}
print(b)
#tạo dict moi nhung học sinh qua mon
v={bien:giatri for bien,giatri in b.items() if giatri >=5}
print(v)
#thư hiên chuyển đỏi dữ liệu trong mục cần chuyển
g= {
    'student':['truong','tuyen','khang','hau','trung','nghia'],
    'score':[5,6,7,8,9,10]
}
bien = pd.DataFrame(g)
print(bien)
#hạn chế của phươn thúe này là in ra hai cột
for bien,giatri in bien.items():
    print(giatri)
#nếu sử dụng thuộc tính iterows sẽ khác phục hạn chế này
for (key,row) in bien.iterrows():
    print(row)