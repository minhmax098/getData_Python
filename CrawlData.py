from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

info_nha = ['title', 'price', 'place', 'date', 'link']
df = pd.DataFrame(columns=info_nha)

# driver
driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe')
url = ['https://muaban.net/mua-ban-nha-dat-cho-thue-toan-quoc-l0-c3?cp=1']


filename = ['nhadattrang1.csv']


def crawInfoFromUrl(url):
    driver.get(url)
    eleList = driver.find_elements_by_class_name("list-item__link")
    itemXPath = '/html/body/main/div[4]/div[1]/div[3]/div[1]/a'
    imageXpath = '/html/body/main/div[4]/div[1]/div[3]/div[1]/a/div[1]/img'
    # itemPrice = '/html/body/main/div[4]/div[1]/div[3]/div[1]/a/div[2]/div[1]/span[1]'
    # / html / body / main / div[4] / div[1] / div[3] / div[1] / a
    # / html / body / main / div[4] / div[1] / div[3] / div[2] / a
    # / html / body / main / div[4] / div[1] / div[3] / div[20] / a

    # / html / body / main / div[4] / div[1] / div[3] / div[20] / a / div[1] / img

    # / html / body / main / div[4] / div[1] / div[3] / div[1] / a / div[1] / img
    # // *[ @ id = "list-box"] / div[1] / a / div[1] / img
    # / html / body / main / div[4] / div[1] / div[3] / div[8] / a / div[1] / img
    # / html / body / main / div[4] / div[1] / div[3] / div[6] / a / div[1] / img

    # *[ @ id = "list-box"] / div[6] / a
    print(eleList)
    index = 0
    i = 1
    try:
        while eleList:
            ele = eleList.pop(0)
            title = ele.get_attribute("title")
            itemUrl = ele.get_attribute("href")
            if i == 7:
                i += 1
            imageXpath = '/html/body/main/div[4]/div[1]/div[3]/div['+ str(i) + ']/a/div[1]/img'
            itemImage = ele.find_element(By.XPATH, imageXpath).get_attribute('src')
            # itemPriceString = ele.find_element(By.XPATH, itemPrice).get_attribute('innerHTML')
            print(title)
            print(itemUrl)
            print(itemImage)
            print(f'Gia tri cua i: {i}')
            # print(itemPriceString)
            i = i + 1
    except Exception as e:
        print(e)

for item in url:
    crawInfoFromUrl(item)
# driver.close()
# driver.quit()

