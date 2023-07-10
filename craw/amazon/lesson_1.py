from requests_html import  HTMLSession
import pandas as pd
from bs4 import BeautifulSoup
s = HTMLSession()
searchterm = 'ssd+card'
url = f'https://www.amazon.co.uk/s?k={searchterm}&i=black-friday'
dealslist = []
def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getdeals(soup):
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    truong = 'https://www.amazon.co.uk/'
    # print(products)
    for bien in products:

        title = bien.find('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).text.strip()
        short_title = bien.find('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).text.strip()[:25]
        link  = bien.find('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']
        try:
            price = bien.find_all('a', {'class': {'a-offscreen'}})[0].text.replace('£','').strip()
        except:
            price = 'none'
        try:
            oldprice = bien.find_all('a', {'class': {'a-offscreen'}})[1].text.replace('£','').strip()
        except:
            oldprice = 'none'
        try:
            reviews = bien.find('span',{'class':'a-offscreen'}).text.strip()
        except:
            reviews =  0
        sale_item  = {
            'title':title,
            'short_title':short_title,
            'link':truong+link,
            'price':price,
            'oldprice':oldprice,
            'reviews':reviews
        }
        dealslist.append(sale_item)
        # print(title,short_title,'\n',link,price,oldprice,reviews)
# soup =getdata(url)
# getdeals(soup)
def get_next_link(soup):
    truong = 'https://www.amazon.co.uk'
    pages = soup.find('span',{'class':'s-pagination-strip'})
    bien =  pages.find('a',{'class':'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})['href']
    # print(bien)
    if not pages.find('a',{'class':'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})['href']:
        url  = pages.find('a',{'class':'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})['href']
        return truong + url
    else:
        return
# get_next_link(soup)

#thuc hien lien tuc qua cac trang khacc nhau
while  True:
    soup = getdata(url)
    getdeals(soup)
    url = get_next_link(soup)
    if not url:
        break
    else:
        print(url)
        print(len(dealslist))

df = pd.DataFrame(dealslist)
print(df.head(10))
df.to_csv('data_2.csv',index=False)