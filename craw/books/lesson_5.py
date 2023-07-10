
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup

def get_product_links(data):
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

def get_product_info(product_links):
    number ={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
    products = []
    for link in product_links:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        info_main  = soup.find('div',class_='col-sm-6 product_main')
        p_tag = info_main.find('p',class_='star-rating')
        star_rating_class = p_tag['class'][1]
        star_rating = star_rating_class.split('-')[-1]
        num_stars = number[star_rating]
        try:
            title = info_main.find("h1").text.strip()
        except:
            title = 'none'
        try:
            price =  info_main.find('p', {'class': 'price_color'}).text.strip()
            price_new = float(price.split('£')[1])
        except:
            price = 'none'
        try:
            available = info_main.select_one("p[class='instock availability']").text.strip()
            available_new = int(available.split()[2].replace('(', ''))
        except:
            available = 'none'
        product = {
            'title':title,
            'price': price_new,
            'available':available_new,
            'num_stars':num_stars
        }
        products.append(product)
    return products

def output(results):
    books = pd.concat([pd.DataFrame(product_list) for product_list in results])
    books.to_csv('books_3.csv',index=False)
    print('saved to csv')
    return

results = []
for i in range(1,50):
    data = get_data(f"https://books.toscrape.com/catalogue/page-{i}.html")
    product_links = get_product_links(data)
    results.append(get_product_info(product_links))
    print(i)
    # time.sleep(1.5)
output(results)
