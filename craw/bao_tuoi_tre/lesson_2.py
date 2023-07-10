import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
cookies = {
    '_uidcms': '1688719114862965968',
    '__uidac': 'ce6df0e243dc7452c658edf6485142a0',
    '_gid': 'GA1.2.1902231767.1688719116',
    '_gat_UA-46730129-1': '1',
    '__RC': '5',
    '__R': '3',
    '_gat_tto_vcc': '1',
    '_ttsid': 'de19742b701a740b3efc34243c972034d165545165f287be546e04ee1f4697b3',
    '_ck_user': 'false',
    '_ck_isTTSao': 'false',
    '_ck_isLogin': 'false',
    '__admUTMtime': '1688719115',
    '_clck': 'jdo8ri|2|fd3|0|1283',
    '__stp': 'eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJhYzBlZjJiMy05ODcwLTQxZmUtOGM2MC1iNGRkNWQ5MDU1MTUifQ==',
    '__stdf': 'MA==',
    '__uif': '__uid%3A5987191151934592664%7C__ui%3A-1%7C__create%3A1688719115',
    '__tb': '0',
    '__IP': '1934592664',
    '_ga_G67558G6BB': 'GS1.2.1688719115.1.1.1688719117.0.0.0',
    '__sts': 'eyJzaWQiOjE2ODg3MTkxMTYwOTQsInR4IjoxNjg4NzE5MTE3MDcxLCJ1cmwiOiJodHRwcyUzQSUyRiUyRnR1b2l0cmUudm4lMkZwaGFwLWx1YXQuaHRtIiwicGV0IjoxNjg4NzE5MTE3MDcxLCJzZXQiOjE2ODg3MTkxMTYwOTQsInBVcmwiOiJodHRwcyUzQSUyRiUyRnR1b2l0cmUudm4lMkYiLCJwUGV0IjoxNjg4NzE5MTE2MDk0LCJwVHgiOjE2ODg3MTkxMTYwOTR9',
    '__stgeo': 'IjAi',
    '_clsk': 'll5t99|1688719117557|1|0|s.clarity.ms/collect',
    'fosp_uid': '0kqgeq0pmre9qxis.1683442248.des',
    'orig_aid': '0kqgeq0pmre9qxis.1683442248.des',
    'fosp_aid': '0kqgeq0pmre9qxis.1683442248.des',
    'fosp_location_zone': '1',
    '_ga': 'GA1.1.836929275.1688719116',
    '_ga_QRFPCFR4FC': 'GS1.1.1688719120.1.0.1688719120.0.0.0',
    'FCNEC': '%5B%5B%22AKsRol9oqUqbB1upsyaFphuQPDAel41OXDZeyrc1J9uAiquq8GtPH4WwE0aSYFtyiR8fOFxCX9ZNDVPmMtbbd8Tt6q9hzxxly6o2cmfdxiS-TL_gosXxgo6lvUH8SDSNwbcXqL8xf8UgMGxTDRo4UpbWgno6u5cLgw%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
    '_ga_8KQ37P0QJM': 'GS1.1.1688719115.1.1.1688719138.37.0.0',
}

headers = {
    'authority': 'tuoitre.vn',
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',# 'cookie': '_uidcms=1688719114862965968; __uidac=ce6df0e243dc7452c658edf6485142a0; _gid=GA1.2.1902231767.1688719116; _gat_UA-46730129-1=1; __RC=5; __R=3; _gat_tto_vcc=1; _ttsid=de19742b701a740b3efc34243c972034d165545165f287be546e04ee1f4697b3; _ck_user=false; _ck_isTTSao=false; _ck_isLogin=false; __admUTMtime=1688719115; _clck=jdo8ri|2|fd3|0|1283; __stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJhYzBlZjJiMy05ODcwLTQxZmUtOGM2MC1iNGRkNWQ5MDU1MTUifQ==; __stdf=MA==; __uif=__uid%3A5987191151934592664%7C__ui%3A-1%7C__create%3A1688719115; __tb=0; __IP=1934592664; _ga_G67558G6BB=GS1.2.1688719115.1.1.1688719117.0.0.0; __sts=eyJzaWQiOjE2ODg3MTkxMTYwOTQsInR4IjoxNjg4NzE5MTE3MDcxLCJ1cmwiOiJodHRwcyUzQSUyRiUyRnR1b2l0cmUudm4lMkZwaGFwLWx1YXQuaHRtIiwicGV0IjoxNjg4NzE5MTE3MDcxLCJzZXQiOjE2ODg3MTkxMTYwOTQsInBVcmwiOiJodHRwcyUzQSUyRiUyRnR1b2l0cmUudm4lMkYiLCJwUGV0IjoxNjg4NzE5MTE2MDk0LCJwVHgiOjE2ODg3MTkxMTYwOTR9; __stgeo=IjAi; _clsk=ll5t99|1688719117557|1|0|s.clarity.ms/collect; fosp_uid=0kqgeq0pmre9qxis.1683442248.des; orig_aid=0kqgeq0pmre9qxis.1683442248.des; fosp_aid=0kqgeq0pmre9qxis.1683442248.des; fosp_location_zone=1; _ga=GA1.1.836929275.1688719116; _ga_QRFPCFR4FC=GS1.1.1688719120.1.0.1688719120.0.0.0; FCNEC=%5B%5B%22AKsRol9oqUqbB1upsyaFphuQPDAel41OXDZeyrc1J9uAiquq8GtPH4WwE0aSYFtyiR8fOFxCX9ZNDVPmMtbbd8Tt6q9hzxxly6o2cmfdxiS-TL_gosXxgo6lvUH8SDSNwbcXqL8xf8UgMGxTDRo4UpbWgno6u5cLgw%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _ga_8KQ37P0QJM=GS1.1.1688719115.1.1.1688719138.37.0.0',
    'referer': 'https://tuoitre.vn/phap-luat.htm',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-requested-with': 'XMLHttpRequest',
}
url = 'https://tuoitre.vn'
def get_link(url):
    # choose = int(input('Enter the number articles: '))
    # choose_new = int(choose/18)
    links = []
    i = 0
    while True:
        i += 1
        response = requests.get(f'https://tuoitre.vn/timeline/6/trang-{i}.htm', cookies=cookies, headers=headers)
        error = response.status_code
        if error != 200:
            break
        soup = BeautifulSoup(response.text, 'lxml')
        link = soup.select("a[class='box-category-link-title']")
        for link_in_news in link:
            href = link_in_news.attrs["href"]
            links.append(url + href)
            print(url+href)
    dict = {'links': links}
    df = pd.DataFrame(dict)
    df.to_csv('list_link_bao_tuoi_tre.csv', index=False)
    print('saved to csv')
    return links
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
def info(links_in_journal):
    products = []
    i =0
    for link in links_in_journal:
        i+=1
        print(i)
        try:
            soup = get_data(link)
            title = soup.select_one('h1').text
            description = soup.select_one('h2').text
            description_new_1 = description.replace("\r\n","")
            description_new_2 = description_new_1.strip()
            content = soup.select("div[class='detail-content afcbc-body']")
            space = ''
            for t in content:
                try:
                    parameters = t.text
                except:
                    parameters = ''
                space += parameters
            content_new = " ".join(space.split())
            content_new = content_new.strip()
            new_data = {
                'title': title,
                'description': description_new_2,
                'content': content_new
            }
            products.append(new_data)
        except:
            pass
    with open('newspapers_new_law_2.json', 'w', encoding='utf-8-sig') as outfile:
        json.dump(products, outfile, indent=4)
    print('Saved to JSON')
links_in_journal = get_link(url)
info(links_in_journal)
