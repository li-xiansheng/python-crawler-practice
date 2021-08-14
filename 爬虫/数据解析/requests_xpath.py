#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from lxml import etree
import requests

# xpath 常用数据解析
# 实例化etree 结合xpath 方法;可结合xpath helper插件使用
if __name__ == '__main__':
    url = "https://www.qiushibaike.com/imgrank/page/2/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    tree = etree.HTML(html)
    # value = tree.xpath('//div[@class="content"]/span//text()')
    value = tree.xpath('//img[@class="illustration"]/@src')

    print(value)
