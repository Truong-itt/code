from tkinter import *
window = Tk()
window.minsize(width=500, height=500)
window.title('toi yeu viet nam')
#tao nhan
#kieeru nhan trong tkinterr
my_label = Label(text='khong sao dau ',font=('Arial',24,'italic'))
my_label.pack()
my_label.config(text='co sao nha')
#tao nut
def action():
    print("Do something")
nut = Button(text="Click Me",command=action)
#tao khung entry
entry = Entry(width=30)
entry.insert(END,'khong co gi day')
entry.pack()

#text
text = Text(width=30,height=5)
text.focus()
#dien noi dung vao text co hoi khac
text.insert(END,"Example of multi-line text entry.")
text.pack()

#Spinbox
def action_2():
    print(my_Spinbox.get())
my_Spinbox = Spinbox(from_=0, to=100,width=10,command=action_2)
my_Spinbox.pack()

#Scale kiểu dữ liệu kéo
#luu y cach in thak nay hoi la
def action_3(gia_tri):
    print(gia_tri)
my_Scale = Scale(from_=0,to=100,command=action_3)
my_Scale.pack()
#kieu du lieu chon nhu khoanh dap an
#diem dac biet la kieu nay se can co mot thak de nghe de lieu
def action_4():
    print(bien_nghe.get())
bien_nghe = IntVar()
radiobutton1=Radiobutton(text='option 1',value=1,variable=bien_nghe,command=action_4);radiobutton1.pack()
radiobutton2=Radiobutton(text='option 2',value=2,variable=bien_nghe,command=action_4);radiobutton2.pack()
radiobutton3=Radiobutton(text='option 3',value=3,variable=bien_nghe,command=action_4);radiobutton3.pack()

#kieu du lieu cuoi list box
ten = ['truong','tuyen','khang','hoa']
my_listbox = Listbox(height=4)
#ham in su kien
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))
    bien = my_listbox.get(my_listbox.curselection())
    if bien == "truong":
        my_listbox.configure(bg="red")
    elif bien == "tuyen":
        my_listbox.configure(bg="yellow")
    else:
        my_listbox.configure(bg="white")
for i in ten:
    my_listbox.insert(ten.index(i),i)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()
window.mainloop()