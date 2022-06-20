from audioop import add
from ctypes import addressof
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ramen_project.settings")

import django
django.setup()

from unicodedata import name
import pandas as pd
import numpy as np
import re
import folium
from urllib.request import urlopen, Request  
from bs4 import BeautifulSoup 
from home.models import Restaurent
import datetime
import time

import warnings
from selenium import webdriver
from selenium.webdriver import ActionChains
warnings.simplefilter(action='ignore')

def crawl_mango():
    url = 'https://www.mangoplate.com/top_lists/2983_ramen2022'
    driver = webdriver.Chrome('static\\chromedriver.exe')

    driver.get(url)
    time.sleep(1)

    element = driver.find_element_by_id('google_ads_iframe_/395211568/init/desktop_all_0')
    driver.switch_to.frame(element)
    tag1 = driver.find_element_by_css_selector('#ad > div > button.ad_btn.ad_close_btn')
    action = ActionChains(driver)
    action.move_to_element(tag1).perform()
    tag1.click()
    driver.switch_to.default_content()
    time.sleep(1)


    for i in range(4):
        tag2 = driver.find_element_by_css_selector('#contents_list > div > button')
        action = ActionChains(driver)
        action.move_to_element(tag2).perform()
        tag2.click()
        time.sleep(2)


    
    req = driver.page_source
    mang = BeautifulSoup(req, 'html.parser')
    mang.prettify()

    name = []
    point = []
    address = []

    list_soup = mang.find_all('div', 'info') 

    for item in list_soup:
        address.append(item.find('p', 'etc').text)
        point.append(item.find('strong', 'point').text.strip())
        title = item.find('span', 'title').text.strip()
        name.append(title[3:])

    name = name[:50]
    point = point[:50]
    address = address[:50]

    data = {
        "Name":name,
        "Point":point,  
        "Address":address
    }

    return data


if __name__=='__main__':
    mango_data = crawl_mango()
    for i in range(len(mango_data['Name'])):
        try:
            Restaurent(name=mango_data['Name'][i], point=mango_data['Point'][i], address=mango_data['Address'][i]).save()
        except:
            print("이미 존재하는 DB입니다.")
            continue




