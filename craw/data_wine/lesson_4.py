from bs4 import BeautifulSoup
import requests
import pandas as pd
productslink = []
data = []
url = 'https://www.thewhiskyexchange.com'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
#tièn hành lấy link

for i in range(1,6):
    r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')
    soup = BeautifulSoup(r.content,'lxml')
    productlist = soup.select("div[class='product-grid'] > ul > li > a")
    for i in productlist:
        link = i.attrs['href']
        link_new = url + link
        productslink.append(link_new)

#lấy info
# for i in productslink:
#     rr = requests.get(i)
#     soup_new = BeautifulSoup(rr.content,header)

#test lay cho 1 phan tu
# url_new = 'https://www.thewhiskyexchange.com/p/45366/kaiyo-mizunara-oak'
for url_new in productslink:
    r = requests.get(url_new,headers=header)
    soup = BeautifulSoup(r.content,'lxml')
    try:
        name = soup.find('h1',class_='product-main__name').text.strip()
    except:
        name = 'NONE'
    # print(name)
    try:
        price = soup.find('p',class_='product-action__price').text.strip()
    except:
        price = 'NONE'
    # print(price)
    try:
        rating = soup.find('span',class_='review-overview__count').text.strip()
        # print(rating)
    except:
        rating = 'do not exits'
        # print(rating)
    dict = {
        'name':name,
        'price':price,
        'rating':rating
    }
    print(f'saved:{name}')
    data.append(dict)
print(data)
df = pd.DataFrame(data)
print(df.head(15))