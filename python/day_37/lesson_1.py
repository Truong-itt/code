import requests
from datetime import datetime
name = "truongdeptrai"
TOKEN = "truongthongthai745"
pixela = 'https://pixe.la/v1/users'
graphID ="grahpi"
#thưuc hiện nhập thông tin vao hệ thống
user_params = {
    "token":TOKEN,
    "username":name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#thưc hiẹn liên kết tạo tài khoản băng thuộc tính post
# response=requests.post(url=pixela,json=user_params)
# print(response.json())

#htư hiện liên kết thcuộ tính post
grap_config = {
    'id':graphID,
    "name":"Cyeling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers ={
    'X-USER-TOKEN':TOKEN
}
grap_endpoint = f"{pixela}/{name}/graphs"
# response = requests.post(url=grap_endpoint,json=grap_config,headers=headers)
# print(response.text)
#thưc hiện tạo bảng pixel
pixel_creation_endpoint = f'{pixela}/{name}/graphs/{graphID}'
#thưc hiện cung cập dữu liêu hàm pixel
#lấy ra thười gian hiện tại
now = datetime.now()
# thưch hiện chuyển đỏi
now_new = now.strftime("%Y%m%y")
# print(type(now_new))
print(now_new)
pixel_data ={
    "date":now_new,
    "quantity":input("how many km?"),
    # "optionalData":
}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data   ,headers=headers)
print(response.text)
# print(pixel_creation_endpoint)
#thưu chiện công đoạn update
update_endpoint=f"{pixela}/{name}/graphs/{graphID}/{now_new}"
#đặt lại kiểu dữ lieệu tru y cập
new_pixel_data ={
    "quantity":"5.5",
    # "optionalData":
}
# response = requests.put(url=update_endpoint,json=new_pixel_data   ,headers=headers)
# print(response.text)
#hiẻu về kiẻu xoá
# deplete_endpoint = f"{pixela}/{name}/graphs/{graphID}/{now_new}"
# response = requests.delete(url=deplete_endpoint,json=new_pixel_data   ,headers=headers)
# print(response.text)
# print(pixel_creation_endpoint)