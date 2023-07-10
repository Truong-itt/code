#ngày được tự do
#hiẻu về applicaton programming interface
#hiểu được sử giao thức với  ipa
#hiêu đơn giản nó là tương tác vớ hệ thông
#tuong tự với việc khách hàng đến nhà hàng goi mon thì món sẽ được thực hiện ở nhà bếp xogn rồi sản phẩm sẽ được đưa đến miệng khách hangf
#ipa đóng vai trò là rào chắn giữa hai cái này và sau đây chúng ta sẽ hiểu về phương thức kết nối với hchúng
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#ktra xem đã kêết nói đươvj với sever chưa
print(response)

if response.status_code == 200:
    print('đa ket nói được với sever hệ thống')
    print(response.json())
    # raise Exception('successfully connect sever')
elif response.status_code != 200:
    raise Exception("bad error do not connection sever")

# 1xx là chờ đợi
# 2 xx là thành công
# 3xx là bạn thực s không có quyền
# 4xx là không có tộn tại
# 5xx máy chủ bị lỗi trong quá trình hoạt động
#sử dụng phuont tính status_code là dùng để trả về trạng thái của dữ liệu

#xem json như một từ điẻn vì thực chất json là một từ đỉn
bien = response.json()['iss_position']
print(f'nhung du lieu lay ra la:{bien}')

#tạo biên tổng truy cập vao hệ thóng
data = response.json()
longitude = data['iss_position']['longitude']
print(longitude)
latitude = data['iss_position']['latitude']
print(latitude)
#gôp dữ liệu thoải mái
all = (longitude,latitude)
print(all)