from tkinter import *
FONT_NAME = "Courier"
from tkinter import messagebox
from random import choice, randint, shuffle
from random import choice, randint, shuffle
import pyperclip
import json
#passswword generation
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)
#save password
def save():
    website = entry_1.get()
    emall = entry_2.get()
    password = entry_3.get()
    new_data = {
        website:{
            'email':emall,
            'password':password
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='Dops',message="Please make sure you haven't left")
    else:
        variable = messagebox.askyesnocancel(title=website,message=f'There are the details entered:\n'
                                                                      f'Email: {emall}\npassword: {password}\n'
                                                                   f'Is it ok to save?')
        if variable:
            try:
                #thưc hiện mở file nhưu bình thường
                with open('file_data.json', 'r') as file:
                    # truy cập đọc tệp data
                    data = json.load(file)
            except FileNotFoundError:
                with open('file_data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('file_data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    # ghi dữ liêu
                    # các phương thức delete này chỉ có tác dụng xoá đi màn hình còn nôi dụng đã truyên fvao file thì sẽ không ảnh hưởng
            finally:
                entry_1.delete(0, END)
                entry_3.delete(0, END)
                entry_2.delete(0, END)
                entry_2.insert(END, '@gmail.com')
                entry_1.focus()

#search password
def find_password():
    website = entry_1.get()
    try:
        with open('file_data.json','r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title=website, message=f'No data file found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            # thực hiện thông bao cho nguòi dung về mật khâu
            messagebox.showinfo(title=website, message=f'Email:{email}\nPassword:{password}')
        else:
            messagebox.showinfo(title=website, message=f'No data file {website} found')


#ut setup
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)
bien =PhotoImage(file='logo.png')
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=bien)
canvas.grid(column=1,row=0)
#setup lable
lable_1 = Label(text='Webiste',highlightthickness=0)
lable_1.grid(column=0,row=1)
lable_2 = Label(text='Email/Username')
lable_2.grid(column=0,row=2)
lable_3 = Label(text='Password')
lable_3.grid(column=0,row=3)
#tao lớp cho người dụng nhập vao
entry_1 = Entry(width=35)
entry_1.focus()
entry_1.grid(row=1,column=1)
entry_2 = Entry(width=60)
entry_2.grid(row=2,column=1,columnspan=2)
entry_2.insert(END,"@gmail.com")
entry_3 = Entry(width=35)
entry_3.grid(row=3,column=1)

#create button
button_1 = Button(text='Generate Password',command=generate_password,width=20)
button_1.grid(column=2,row=3)
button_2 = Button(text='Add',command=save,width=51)
button_2.grid(row=4,column=1,columnspan=2)
#button search
button_3 = Button(text='Search',command=find_password,width=20)
button_3.grid(column=2,row=1)

window.mainloop()