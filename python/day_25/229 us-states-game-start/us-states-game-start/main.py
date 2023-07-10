import turtle
import  pandas
#đoc file
data = pandas.read_csv('50_states.csv')
print(data)
#tận dụng thuộc tính chuyển dổi tên tiêu ban thhành llist cho tiện việc ktra
all_State = data.state.to_list()
print(all_State)
screen = turtle.Screen()
screen.title('subcommittee in america')
image = 'blank_states_img.gif'
#addshape thuộc tính mới này có tác dụng thêm hình ảnh mơi tùe bên ngoài vào background trong turtle
screen.addshape(image)
turtle.shape(image)

#toa hop thoai cho nguoi dung
guess = []
while len(guess) < 50:
    answer_State = screen.textinput(title=f'{len(guess)}/50 Guess the state',prompt="what's annther state's name?").title()
    print(answer_State)
    if answer_State == 'Exit':
        danh_sach_miss = []
        #lấy ra cac sô không có trong việc trả lời
        for i in all_State:
            if i not in guess:
                danh_sach_miss.append(i)
        # print(danh_sach_miss)
        #lấy bỏ làm một file bỏ lỡ csv bằng pandas
        new_data =  pandas.DataFrame(danh_sach_miss)
        print(new_data)
        break
    if answer_State in all_State and answer_State not in guess:
        i = turtle.Turtle()
        i.hideturtle()
        i.penup()
        bien_location = data[data['state'] == answer_State]
        i.goto(int(bien_location.x),int(bien_location.y))
        i.write(answer_State)
        guess.append(answer_State)

#tạo khung câu hỏi cho turtle để ngươi dùng nhập vao
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#bắt đâu vòng lập chính trong turtle
#to tên của các tiểu ban thànhmột list câu trl của người dùng

turtle.mainloop()

# screen.exitonclick()