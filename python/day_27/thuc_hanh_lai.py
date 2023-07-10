#hieu nhanh ve thu vien tkinter lai
#ok ready
from tkinter import *
window = Tk()
window.minsize(width=500, height=500)
window.title('toi yeu viet nam')

#kieeru nhan trong tkinterr
my_label = Label(text='khong sao dau ',font=('Arial',24,'italic'))
my_label.pack()
my_label.config(text='co sao nha')
#pack place grid

#kieu nut trong tkinter
def kkk():
    bien = my_entry.get()
    my_label.config(text=bien)
    print(bien)
my_button = Button(text='click me',command=kkk)
my_button.pack()


#entry
my_entry = Entry(width=30)
my_entry.pack()
window.mainloop()


#câu chuyện ngoài lề hiẻu về chuyền biến trong hàm
# def add_1(*bien):
#     tong = 0
#     for i in bien:
#         tong += i
#     return tong
# print(add_1(1,2,3))
#ứng dụng kiểu này dùng cho kiểu dict
# def add_2(n,**bien):
#     print(bien)
#     n += bien['truong']
#     n *= bien['tuyen']
#     print(n)
# add_2(2,truong=4,tuyen=2)
# #mot vai luu y va kieu class
# class car:
#     def __init__(self,**bien):
#         self.ten = bien.get('ten')
#         self.ngay_sinh = bien.get('ngay_sinh')
#         self.gioi_tinh = bien.get('gioi_tinh')
# xin_chao = car(ten='truong',ngay_sinh='19/10/2000')
# print(xin_chao.ten);print(xin_chao.gioi_tinh)