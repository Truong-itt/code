# file = open("file.txt")
# with open("file.txt") as file:
    # contens = file.read()
    # print(contens)
# file.close()
import fileinput

# with open("file.txt",mode="a") as file:
#     file.write("\nanh yeu em")
# with open("file.txt") as file:
#     bien = file.read()
#     print(bien)

# fỉle = open("file.txt")
# contens = fỉle.read()
# print(contens)
# fỉle.close()
#mở kiểu này cần phải đong lại

with open("file.txt") as file:
    contens = file.read()
    print(contens)

with open("file.txt",mode= "w") as file:
    file.write("\n em co yeu anh khong nhi")

with open("file.txt") as file:
    contens = file.read()
    print(contens)
with open("file.txt",mode="a") as file:
    for i in range(5):
        file.write("\nem khong thuong anh ha")
with open("file.txt") as file:
    contens = file.read()
    print(contens)

f = open("file_2.txt","x")
