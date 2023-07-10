import requests
from bs4 import BeautifulSoup
import pandas
productlink = []
data = []
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

main_product_list = []
for i in range(1, 6):
    url = f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={i}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    productlist = soup.se("div[class='product-grid'] > ul > li > a")
    main_product_list.extend(productlist)
print(*main_product_list, sep="\n")
print(len(main_product_list))
# for link in main_product_list:
#     hhh = f'https://www.thewhiskyexchange.com{link}'
#     # hhh = truong
#     response_2 = requests.get(hhh, headers=headers)
#     soup_2 = BeautifulSoup(response_2.content, 'lxml')
#     name_product = soup_2.find("h1", class_="product-main__name").text.strip()
#     prize = soup_2.find("p", class_="product-action__price").text.strip()
#     try:
#         rating = soup_2.find("span", class_="review-overview__count").text
#         review_count = rating.replace('Reviews', '')  # Loại bỏ chữ "Reviews"
#         review_count = ''.join(filter(str.isdigit, review_count))  # Lấy các ký tự số
#     except:
#         rating = 'do not exits'
#     whisky = {
#         'name': name_product,
#         'rating': review_count,
#         'price:': prize
#     }
#     data.append(whisky)
# for i in data:
#     print(i)
#     print(name_product)
#     print(prize)
#     print(rating,'\n\n')

# print(*main_product_list, sep="\n")
# print(len(main_product_list))