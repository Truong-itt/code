#thực hành lại tìm hiểu về thư viện tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
#xử lí reset và dâu tick cho chương trinhf
#phương thức after_cancel này có tác dụng cho thuộc tính tời gian được xử dụng vè 0
def reset_timer():
    window.after_cancel(timer)
    #một số công việc cần xư lí xong xong
    #timer_text 00:00
    #title_lable 'timer'
    #reset check map
    canvas.itemconfig(timer_text, text=f'00:00')
    title_lable.config(text='Timer')
    check_button.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
#tạo biên giá trị cho nut bấm khi ta ấn vao sẽ thực hiện một chức nắng cụ the
#xây dựng cho hàm có thể lặp lại đúng tần xuất nhưu đồng hồi prômdỏo
def start_time():
    global reps
    reps  += 1
    #chuyển đổi giữa phút và giây cho hchương trình
    #tháy đổi những biên có sẳn
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #quy định các mốc thời gian cho chương trình chạy
    # count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text='Break',fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text='Break',fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text='Work',fg=GREEN)
        mark = ''
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += '✔'
        check_button.config(text=mark)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#viết hàm tình thời gian ngược cho chương trình
#xây dựng hàm và sẽ gọi hàm
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    coun_second = count%60
    #ktra chúng ta sẽ không đẻ hàm chạy khi bé hơn 0
    #không in trong terminal mà chuyển sang in trên máy
    canvas.itemconfig(timer_text,text = f'{count_min}:{coun_second}')
    if coun_second == 0:
        canvas.itemconfig(timer_text, text=f'{count_min}:00')
    if coun_second < 10:
        canvas.itemconfig(timer_text, text=f'{count_min}:0{coun_second}')
    if count > 0:
        timer = window.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
#hiển thị set up lên màn hình
window = Tk()
#tiêu đề cho tkinter
window.title('promodoro')
#đặt cách điệu trong đồng hồ ra bên ngoài
window.config(padx=100,pady=50,bg=YELLOW)
#sư dụng thuọc tinsh window after khi muôn một sự kiện gì đấy diễn ra sao bao nhiêu phần trăm của giấy

#tạo lable cho đồng hô
#cài màu cho chữ băng fg
title_lable = Label(text='Timer',fg=GREEN,font=(FONT_NAME,35,'bold'),bg=YELLOW)
title_lable.grid(column=1,row=0)
#thiết lập cho màu viền cũng nhu viền được hài hoà với thực cành
canvas  = Canvas(width= 200,height=224,bg=YELLOW,highlightthickness=0)
#canvas cho phép ta làm nhiểu thứ kể cả chèn text lên một lớp có sănt
#thiết lặp sănc tạo độ để đặt ảnh vào
bien = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = bien)
#thiết lập đaonj text trong trân canvas vừa thiế lập
#dùng các thuộc tính đẻ cài đặp cho lớp
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
#dùngg hàm in ra hình vừa thiết lập
canvas.grid(column=1,row=1)
#thiết lập các nút cần thiết cho chương trình
start_button = Button(text='Start',highlightthickness=0,command=start_time)
start_button.grid(column=0,row=2)
reset_button = Button(text='Reset',highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)
#thiêt lập chẹc map
check_button = Label(highlightthickness=0,bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,'bold'))
check_button.grid(column=1,row=3)
# count_down(5)
window.mainloop()
#thiết lặp lại cho viêt lên màn hình tránh tình tranhg chạy một lần
#việc tiếp theo cần làm là thiết lâpj lại những nút và lable trong lâpj trình tkinter
#công việc tạo lại app đồng hồ cơ bản đã hoan thiện và đã hiểu