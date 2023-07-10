import colorgram

# Trích xuất 6 màu sắc từ hình ảnh "image.jpg"
colors = colorgram.extract("anh.jpg", 6)

# In ra các giá trị RGB của các màu sắc
danh_sach_mau_trich_xuat = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    danh_sach_mau_trich_xuat.append(new_color)
print("\n")
print(danh_sach_mau_trich_xuat)