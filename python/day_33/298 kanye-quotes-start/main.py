from tkinter import *
import requests

def get_quote():
    #thưc hiện kết nối đên dữ liệu trung tâm
    respoonse = requests.get(url="http://api.open-notify.org/iss-now.json")
    respoonse.raise_for_status()
    # raise_for_status thuộc tính này ktra đã kết nói ở api 2xx chưa nêý chưa bao lối
    #tiến hanh liên kết dữ liệu json
    data = respoonse.json()
    print(data)
    quote = data["timestamp"]
  #thay đôi dữ liệu săn có trong bộ dữ liệu
    canvas.itemconfig(quote_text,text = quote)





window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()