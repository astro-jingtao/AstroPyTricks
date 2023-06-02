#!/usr/bin/env python3
#-*coding:utf-8 -*-
import os
import time
import shutil
from urllib import request
from bs4 import BeautifulSoup
import re
url = r'https://arxiv.org/list/astro-ph.CO/recent'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
page = request.Request(url,headers= headers)
page_info = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(page_info,'html.parser')
links = soup.find_all('a',href=re.compile("^/pdf/"))
for link in links:
    print(link.attrs['href'][5:]+r'.pdf')
    if  link.attrs['href'][5:]+r'.pdf' in os.listdir():
        print(r'you have already read this paper')
        continue
    else:
        request.urlretrieve(r'https://arxiv.org'+link.attrs['href'],r'./'+link.attrs['href'][5:]+r'.pdf')
url = r'https://arxiv.org/list/astro-ph.GA/recent'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
page = request.Request(url,headers= headers)
page_info = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(page_info,'html.parser')
links = soup.find_all('a',href=re.compile("^/pdf/"))
for link in links:
    print(link.attrs['href'][5:]+r'.pdf')
    if  link.attrs['href'][5:]+r'.pdf' in os.listdir():
        print(r'you have already read this paper')
        continue
    else:
        try:
            request.urlretrieve(r'https://arxiv.org'+link.attrs['href'],r'./'+link.attrs['href'][5:]+r'.pdf')
        except:
            request.urlretrieve(r'https://arxiv.org'+link.attrs['href']+r'.pdf',r'./'+link.attrs['href'][5:]+r'.pdf')

os.system('open complete.wav')
os.system('open ./')
