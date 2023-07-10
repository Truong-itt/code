BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
to_learn ={}
#tạo một dict rỗng để lưu dữ liệu dừng đọc qua
current_card= {}
#trích xuất dưc liệu pandas
#thừ vói trường hợp không truy xuất dữ  liệu được
try:
    data = pandas.read_csv('data/french_words.csv')
except FileNotFoundError:
    nguyenmau = pandas.read_csv('data/french_words.csv')
    print(nguyenmau)
    to_learn = nguyenmau.to_dict(orient='records')
else:
    # chuyên data thành kểu dict cho dễ quảng lí
    to_learn = data.to_dict(orient='records')

# print(to_learn)
#thiết lạp các hàm trong lập trình python
#thiết lập cho màn hình có nhữn thuộc tính nhất dịnh ở đay là flip_word

#thuoc tinsh doi mau trong canvas la fill
def next_card():
    #trich xuất dữ liệu
    global current_card,bien
    window.after_cancel(bien)
    current_card=random.choice(to_learn)
    # print(f'Current card:{current_card}]')
    #thưch hiện thay đổi trên giao diện
    canvas.itemconfig(card_tittle, text = 'French',fill = 'black')
    canvas.itemconfig(card_word,text = current_card['French'],fill = 'black')
    canvas.itemconfig(card_background,image = canvas_front_img)
    # thiêt lập cho ảnh tự lật sao 3 giây
    bien = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_tittle,text = 'English',fill = 'white')
    canvas.itemconfig(card_word,text = current_card['English'],fill = 'white')
    canvas.itemconfig(card_background,image = card_back)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    #sêp dữ liệu lại cho thành cái frame
    đata = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv',index=False)
    next_card()
# thiết lâpj đisplay cho phan mem
window = Tk()
window.title('FLashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
bien = window.after(3000, func=flip_card)
#thực hiện chèn ảnh và thuọc tính bang canvas
#cái này bang với bakcground đưucọ tạo
canvas = Canvas(width=800,height=526)
card_back = PhotoImage(file='images/card_back.png')
canvas_front_img = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400,263,image = canvas_front_img)
#fic loõi màn hình cho xoá dường viển
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
#thiết lập vị trí cho màn hình
#chèn đoạn text cho đoạn code
card_tittle = canvas.create_text(400,150,text='',font=('Ariel',40,'italic'))
card_word = canvas.create_text(400,263,text='',font=('Ariel',40,'italic'))
canvas.grid(row=0,column=0,columnspan=2)
#thiết lập các nút cho bàn phóm
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)
check_button = PhotoImage(file='images/right.png')
known_button = Button(image=check_button,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)
next_card()
# thiết lập cho màn ihfnh
#van de xu li nhung tu nguoi dung da gap roi chi lay nhung tu moi thoi
window.mainloop()
