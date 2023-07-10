#thuc hien cao web boooks
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# url  = "https://books.toscrape.com/catalogue/page-2.html"
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup
# bien = get_data(url)
# print(bien)

def link_products(data):
    truong ='https://books.toscrape.com/catalogue/'
    results = data.select("li[class='col-xs-6 col-sm-4 col-md-3 col-lg-3'] > article[class='product_pod'] > h3 > a")
    links = []
    links_products = []
    for bien in results:
        href = bien.attrs["href"]
        links.append(href)
    for link in links:
        link_product = truong+link
        links_products.append(link_product)
    return links_products
# link = link_products(bien)
# print(*link,sep='\n')
def get_info_products(link_products):
    color ='#E6CE31'
    products = []
    for bien in link_products:
        r = requests.get(bien)
        soup = BeautifulSoup(r.text, 'lxml')
        number ={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
        # print(r)
        # print(soup)
        info_main  = soup.find('div',class_='col-sm-6 product_main')
        p_tag = info_main.find('p',class_='star-rating')
        star_rating_class = p_tag['class'][1]
        star_rating = star_rating_class.split('-')[-1]
        num_stars = number[star_rating]
        # for star in star_tags:
        #     if star.get('style') == 'color: #f8ce0b;':
        #         num_stars += 1
        # print(info_main)
        try:
            title = info_main.find("h1").text.strip()
        except:
            title = 'none'
        try:
            price =  info_main.find('p', {'class': 'price_color'}).text.strip()
        except:
            price = 'none'
        try:
            availible = info_main.select_one("p[class='instock availability']").text.strip()
        except:
            availible = 'none'
        product = {
            'title':title,
            'price': price,
            'availible':availible,
            'num_star':num_stars
        }
        products.append(product)
    return products
# info = get_info_products(link)
# print(*info,sep='\n')

def ouput(game_list_very_many):
    books = pd.concat([pd.DataFrame(game_list_50) for game_list_50 in game_list_very_many])
    books.to_csv('books.csv',index=False)
    print('saved to csv')
    return

results = []
# results.append(info)
# ouput(results)
for i in range(1,50):
    data = get_data(f"https://books.toscrape.com/catalogue/page-{i}.html")
    link_products = link_products(data)
    results.append(get_info_products(link_products))
    print(i)
    # time.sleep(1.5)
ouput(results)
