#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from lxml import etree
import requests

# 使用验证码分析工具....略
# 登陆后使用cookie 持续访问
if __name__ == '__main__':
    # ******创建session对象*********
    session = requests.Session()
    url = "https://www.qiushibaike.com/imgrank/page/2/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }

    response = session.get(url=url, headers=headers)
    html = response.text
    tree = etree.HTML(html)
    # value = tree.xpath('//div[@class="content"]/span//text()')
    value = tree.xpath('//img[@class="illustration"]/@src')

    print(value)
    response1 = session.post(url,  headers=headers)
    print(response1.text)
