# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:11:34 2023

@author: Rodrigo
"""
import urllib
from bs4 import BeautifulSoup

url = input('Enter: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))