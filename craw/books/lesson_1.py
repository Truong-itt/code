#thuc hien cao web boooks
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# url ='https://books.toscrape.com/'
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup
# print(get_data(url))
# data = get_data(url)
def link_products(data):
    truong ='https://books.toscrape.com/'
    #thuc hien  lay thong tin cua mot san pham
    results = data.select("li[class='col-xs-6 col-sm-4 col-md-3 col-lg-3'] > article[class='product_pod'] > h3 > a")
    # print(results)
    links = []
    links_products = []
    for bien in results:
        href = bien.attrs["href"]
        links.append(href)
    for link in links:
        link_product = truong+link
        # print(link_product)
        links_products.append(link_product)
    return  links_products
# pause(data)

def get_info_products(link_products):
    color ='#E6CE31'
    products = []
    for bien in link_products:
        time.sleep(1.5)
        r = requests.get(bien)
        soup = BeautifulSoup(r.text, 'lxml')
        info_main  = soup.find('div',class_='col-sm-6 product_main')
        p_tag = info_main.find('p',class_='star-rating')
        star_tags = p_tag.find_all('i',class_='icon-star')
        num_stars = 0
        price =  info_main.find('p', {'class': 'price_color'}).text.strip()
        # price_new = int(price.split()[2].replace('(', ''))
        availible= info_main.select_one("p[class='instock availability']").text.strip()
        # availible_new = availible.split('£')[1]
        for star in star_tags:
            if star.get('style') == 'color: #f8ce0b;':
                num_stars += 1
        product = {
            'title':info_main.find("h1").text.strip(),
            'price':price,
            'availible':availible,
            'num_star':num_stars
        }
        products.append(product)
    # print(*products,sep='\n')
    return products
#-> ham nay tra ve mot cai list day du




#-> ham nay gop cac datframe khác nhau lai
def ouput(game_list_very_many):
    #thuc hiẹn chuyenh thanh dataframe
    books = pd.concat([pd.DataFrame(game_list_50) for game_list_50 in game_list_very_many])
    #thuc  hien lay khong  bao gom chi muucdu lieu vì nhưng lần 50 gôp lại sẽ bị sai
    books.to_csv('books.csv',index=False)
    print('\nsaved to csv')
    return

results = []
for i in range(0,50):
    #duong dan url main duoc thay doi 50 lan
    data = get_data(f"https://books.toscrape.com/catalogue/page-{i}.html")
    link_products = link_products(data)
    results.append(get_info_products(data))
    time.sleep(1.5)
ouput(results)
