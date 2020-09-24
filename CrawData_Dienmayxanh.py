from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# crawl_data từ trang điện máy xanh
info_dienmayxanh = ['']
df = pd.DataFrame(columns= info_dienmayxanh)

# import driver
driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe')
url = ['https://www.dienmayxanh.com/may-giat/wcv10612xb0st?itm_source=gs-ce-trang-chu']


filename = ['dienmayxanh.csv']


def CrawlInfoFromUrl(url):
    driver.get(url)
    eleList = driver.find_element_by_class_name("list-item_link")
    itemXPath = ''
    imageXPath = ''


    #in ra cái eleList
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
            imageXPath = ''
            itemXPath = ""



