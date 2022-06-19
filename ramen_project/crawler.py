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

def crawl_mango():
    url = 'https://www.mangoplate.com/top_lists/2983_ramen2022'
    req = Request(url, headers={'User-Agent': 'Chrome'})  
  
    html = urlopen(req)
    mang = BeautifulSoup(html, 'html.parser')
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

    name = name[:10]
    point = point[:10]
    address = address[:10]

    data = {
        "Name":name,
        "Point":point,
        "Address":address
    }
    
    return data


if __name__=='__main__':
    mango_data = crawl_mango()
    for i in range(10):
        Restaurent(name=mango_data['Name'][i], point=mango_data['Point'][i], address=mango_data['Address'][i]).save()




