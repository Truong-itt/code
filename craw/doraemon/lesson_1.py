import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


url  = 'https://nhasachmienphi.com/truyen-tranh-doremon.html'
def get_data(url):
    r = requests.get(url)
    # print(r.status_code)
    soup  = BeautifulSoup(r.text,'lxml')
    # print(soup)
    return soup
data = get_data(url)

def get_product_link(data):
    item_ch_mora = data.find_all("div", class_=["item_ch_mora", "item_ch_mora hide_item"])
    list_link = [bien.find("a")['href'] for bien in item_ch_mora]
    return list_link

list_link =get_product_link(data)
# print(*list_link,sep='\n')
def get_info(list_link):
    #truy cap vao lay ra titile va anh
    products = []
    t = 0
    for link in list_link:
        # time.sleep(3)
        #chua thuc hien truy cap vao du lieu
        t += 1
        print(t)
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text,'lxml')
            title = soup.find("h2").text
            list_image = soup.select("img[class='truyen-tranh']")
            img_tags = [img_tag.get('src') for img_tag in list_image]
        except:
            title = 'none'
            img_tags ='none'
        product  ={
            'title':title,
            'image':img_tags,
        }
        products.append(product)
    df = pd.DataFrame(products)
    df.to_csv(f'tuyen_tap_doremon.csv',index=False, encoding='utf-8-sig')
    print(*products,sep='\n')
get_info(list_link)
