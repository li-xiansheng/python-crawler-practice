#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

import requests

# Re 模块正则匹配提取数据
# 正则匹配提前数据
if __name__ == '__main__':
    url = "https://www.qiushibaike.com/imgrank/page/2/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    list = re.findall(ex, html, re.S)

    print(list)
