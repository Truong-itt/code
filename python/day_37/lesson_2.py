#thưc hiện liên kết với thư vien j
import requests
from datetime import datetime
name = "truongdeptraiqua"
TOKEN = "truongthongthai745"
pixela = 'https://pixe.la/v1/users'
graphID ="grahpi"
#bước 1 tạo user
user_params = {
    "token":TOKEN,
    "username":name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#thưc hiện liên kết
# response = requests.post(url=pixela,json=user_params)
# print(response.text)
#bươcs tiếp theo tạ cho các thuộc tính và nạp tk
grap_config = {
    'id':graphID,
    "name":"Cyeling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
#chú tính bao gòm id biểu đò tên biểu đò đơn bị màu sắc kiểu dữ liệu truyền vao
#tạo liên kết theo dạng POST - /v1/users/<username>/graphs
#thưc hiện toạ liên kết hệ thống
header ={
    'X-USER-TOKEN':TOKEN
}
grap_endpoint = f"{pixela}/{name}/graphs"
# response = requests.post(url=grap_endpoint,json=grap_config,headers=header)
# print(response.text)
#truy vập tạo bằng đồ hiện