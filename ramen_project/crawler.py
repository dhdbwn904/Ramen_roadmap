from audioop import add
from ctypes import addressof
import os, json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ramen_project.settings")
from django.core.exceptions import ImproperlyConfigured

import django
django.setup()

from unicodedata import name
import pandas as pd
import numpy as np
import re
import folium
import googlemaps
from urllib.request import urlopen, Request  
from bs4 import BeautifulSoup 
from home.models import Restaurent
from datetime import datetime
import time
from pathlib import Path


import warnings
from selenium import webdriver
from selenium.webdriver import ActionChains
warnings.simplefilter(action='ignore')

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR / 'ramen_project', 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_variable(key):
    try:
        return secrets[key]
    except:
        print("Exception occured")
        

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
    lat = []
    lng = []
    img = []
    review = []

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

    list_soup = mang.find_all('div', 'with-review')

    for item in list_soup:
        try:
            img.append(item.find('img', 'center-croping lazy')['data-original'])
        except:
            continue

    print(img)

    img = img[:50]
    data['img'] = img

    gmaps_key = get_variable("API_KEY")
    gmaps = googlemaps.Client(gmaps_key)

    for i in range(len(data['Address'])):
        lat.append(gmaps.geocode(data['Address'][i])[0].get('geometry')['location']['lat'])
        lng.append(gmaps.geocode(data['Address'][i])[0].get('geometry')['location']['lng'])

    data['lat'] = lat
    data['lng'] = lng

    return data


if __name__=='__main__':
    mango_data = crawl_mango()
    for i in range(len(mango_data['Name'])):
        try:
            Restaurent(name=mango_data['Name'][i], point=mango_data['Point'][i], address=mango_data['Address'][i], lat=mango_data['lat'][i], lng=mango_data['lng'][i], img=mango_data['img'][i]).save()
        except:
            print("이미 존재하는 DB입니다.")
            continue




