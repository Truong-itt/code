import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import  time

url = 'https://tuoitre.vn/phap-luat.htm'
os.environ['PATH'] += r";C:\Development"
driver = webdriver.Chrome()



def scroll_down(url):
    i = 0
    while True:
        i += 1
        try:
            driver.execute_script("window.scrollBy(0, 500);")
            add = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/div[1]/div/div[4]')
            if add:
                add.click()
            print(i)
        except:
            break
def get_article_links(url):
    # Mở trang web
    driver.get(url)
    time.sleep(5)

    # Cuộn xuống để tải thêm bài báo
    scroll_down(url)

    # Tìm tất cả các liên kết bài báo trên trang
    links = driver.find_elements_by_xpath('//a[@class="link-news"]')

    article_urls = []
    for link in links:
        article_url = link.get_attribute("href")
        article_urls.append(article_url)

    return article_urls


# URL trang bạn cần thu thập bài báo
url = "https://tuoitre.vn/phap-luat.htm"

# Lấy danh sách các đường dẫn bài báo
article_urls = get_article_links(url)

# In danh sách đường dẫn bài báo
for article_url in article_urls:
    print(article_url)

# Đóng trình duyệt
driver.quit()
