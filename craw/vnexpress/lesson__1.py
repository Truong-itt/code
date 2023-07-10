import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import json
url = "https://vnexpress.net/phap-luat?gidzl=35v_6xyfeZ0EGNSVi3-YD01BT1-eEF8s7afmI_erh354H70Qz62dEa4LTXQcOQK_5nOZ7ZU6HkGPk26fDW"
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    return soup
def get_news_links(link):
    linkss = []
    for bien in range(1,21):
        time.sleep(1)
        variable = f"https://vnexpress.net/phap-luat-p{bien}"
        soup = get_data(variable)
        links = soup.select("h3[class='title-news'] > a")
        for i in links:
            href = i['href']
            linkss.append(href)
    # print(*linkss,sep='\n')
    return linkss

links_all = get_news_links(url)
def get_contents(links_all):
    products = []
    ttt = 0
    for i in links_all:
        print(i)
        ttt +=1
        print(ttt)
        bien = get_data(i)
        try:
            title = bien.select_one("h1[class='title-detail']").text
        except:
            title = 'none'
        try:
            description = bien.select_one("p[class='description']").text
        except:
            description = 'none'
        try:
            content = bien.select("p[class='Normal']")
            # content_one = []
            content_one = ""
            for i in content:
                bien = i.text
                content_one += bien
                # content_one.append(bien)
                # content_one = content_one
        except:
            content_one = 'none'
        product = {
            'title':title,
            'description':description,
            'content':content_one
        }
        print(product)
        products.append(product)
    print(*products,sep='\n')
    return products
products_infos = get_contents(links_all)
def output(products_infos):
    # fill missing keys with None
    keys = set().union(*products_infos)
    for info in products_infos:
        info.update({k: None for k in keys - info.keys()})
    # write to JSON file
    with open('newspapers_new_law_2.json', 'w',encoding='utf-8-sig') as outfile:
        json.dump(products_infos, outfile,indent = 4)
    print('Saved to JSON')

output(products_infos)