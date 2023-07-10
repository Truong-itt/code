import requests
from bs4 import BeautifulSoup
import pandas
import time
productlink = []
data = []
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

for i in range(1,6):
    url = f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={i}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #lay ra danh sach san pham
    produclist =soup.select("div[class='product-grid'] > ul > li")
    for i in produclist:
        link = i.find('a', class_='product-card')['href']
        # print(link)
        productlink.append(link)

ttt ='https://www.thewhiskyexchange.com/p/39382/karuizawa-1970-cask-1985'
bien = requests.get(ttt)
print(bien.status_code)
for link in productlink:
    time.sleep(1)
    ttt = f'https://www.thewhiskyexchange.com{link}'
    bien = requests.get(ttt,headers=headers)
    print(bien.status_code)
    name_product = bien.find("h1", class_="product-main__name")
    print(name_product)
