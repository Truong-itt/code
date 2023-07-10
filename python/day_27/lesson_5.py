from tkinter import *
import math
window = Tk()
#tránh sử dụng áp cứng nhyw này
# window.minsize(width=200,height=100)
window.title('xin chao mn')
window.config(padx=20,pady=20)
#tạo nhan dan
label_1 = Label(text='Is equal to',font=('Arial',15,'normal'))
label_1.grid(column=0,row=1)
label_2 = Label(text='Miles',font=('Arial',15,'normal'))
label_2.grid(column=2,row=0)
label_3 = Label(text='Km',font=('Arial',15,'normal'))
label_3.grid(column=2,row=1)
#lable thay đoi
label_4 = Label(text='0',font=('Arial',15,'normal'))
label_4.grid(column=1,row=1)
# label_4.config(padx=10,pady=10)
#tao mot nut de an vao
def convert():
    bien_1 = float(input.get())
    km = bien_1 * 1.609344
    label_4.config(text=f'{round(km,2)}')
nut = Button(text='calculate',command=convert)
nut.grid(column=1,row=2)
#the input cho phép ngươfi dùng nhập vao nội dung chuyển dổi
input = Entry(width=10)
input.grid(column=1,row=0)
window.mainloop()