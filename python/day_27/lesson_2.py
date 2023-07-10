#hiểu về truyên đôisôs là như thế noà
def add(*a):
    tong =0
    print(a[0])
    for i in a:
        tong += i
    return tong
print(add(1,3,4,5,1))
#hiuểu về truyên theo kiểu dict

def add2(**bien):
    print(type(bien))
    print(bien)
    for key,value in bien.items():
        print(key)
        print(value)
add2(bien='truong',bien2='khang',bien3='trong')
#khi truyen một biên đơn tử bên ngoài vào
def add3(n,**bien):
    print(type(bien))
    print(bien)
    for key,value in bien.items():
        print(key)
        print(value)
    n += bien['bien1']
    n *= bien['bien2']
    print(n)
add3(2,bien1=2,bien2=4)
#hiẻu về phương thức truyền trong clas
class car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('mau_vang')
my_car = car(make='truong',model='truong dep trai')
print(my_car.model)
print(my_car.colour)
#nếu truyền vào mà không có đẻ lấy ta thì sẽ sinh ra lỗi
#khắc phucj như sau
# thêm chữ get vào lfa đươc