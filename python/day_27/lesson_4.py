from tkinter import *
#tạo ra của sổ window
window = Tk()
window.title('Widget Examples')
window.minsize(width=500,height=500)
#tao  nhan
lable = Label(text="This is old text")
lable.config(text='This is new text')
# lable.pack()
lable.grid(column=0,row=0)
lable.config(padx=50,pady=50)
#tạo nút
#tao nut và gan ham cho nut
def action():
    print("Do something")
#gọi hàm chạy nut
button = Button(text='Click Me',command=action)
button.grid(column=1,row=1)
#tạo ra một button mới theo
button_new = Button(text='button new',command=action)
button_new.grid(column=2,row=0)
#tạo entry cho ngừo idùng điẹn vào
entry = Entry(width=30)
#them thuộc tính vào =entry
entry.insert(END,'Some text to begin with.')
print(entry.get())
entry.grid(column=3,row=2)

window.mainloop()