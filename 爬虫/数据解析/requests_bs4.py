#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import requests

# bs4 熟悉定位提取数据
# bs4 BeautifulSoup模块api解析
if __name__ == '__main__':

    url = "https://www.qiushibaike.com/imgrank/page/2/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    img = soup.findAll('img', {'class': 'illustration'})
    for value in img:
        print(value.get('src'))
