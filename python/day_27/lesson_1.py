import tkinter
window = tkinter.Tk()
window.title('toi yeu viẹt nam')
window.minsize(width=500,height=300)

#label
bien = tkinter.Label(text='toi la truong',font=('Arial',24,'italic'))
# bien.pack(side='right')
#cach đẻ cho phần tử được in ở chính giữa
# bien.pack(expand=True)
bien.pack()
#hai cách thay đổi thuộc tính đã áp dụng cho phần tử
# bien['text']='anh yeu em lam'
bien.config(text='anh yeu em')

#toạ nút trong tkinter
def convert():
    print('i got clicked')
    bien1 = input.get()
    bien.config(text=bien1)
nut =  tkinter.Button(text='click me',command=convert)
nut.pack()

#tạo đầu vào trong tkinter
input = tkinter.Entry(width=10)
input.pack()
print(input.get())
window.mainloop()