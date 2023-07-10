# class cha:
#     def __init__(self,txt):
#         self.toi = "yeu viet nam, và cả yêu em"
#         self.bien = 10
#         self.bienn = txt
#     def inn(self):
#         print(self.toi)
#     def in_txt(self):
#         print(self.bienn)
# class con(cha):
    #có thể nhâận lấy toàn bộ từ lớp cha đồng thời thêm biên txt vào
    # def __init__(self,txt):
    #     super().__init__(txt)
    #bạn cũng có thể dùng lại hàm của thak cha
#     def tai_che(self):
#         super().inn()
#
#
# y = cha("yeu con nhiẻu lăm con yêu ạ")
# y.in_txt()
# y.inn()
#
#
# v = con("yeu đong bao")
# v.inn()
# v.in_txt()
# v.tai_che()
class bien:
    def __init__(self,bien):
        self.a = bien
    def inn(self):
        self.a += 10
        print(self.a)
e = 5
t= bien(e)
t.inn()
print(e)