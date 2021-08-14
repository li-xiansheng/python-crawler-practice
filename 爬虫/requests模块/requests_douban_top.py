#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

# UA 伪装
if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    kw = input('enter a word:')
    param = {
        'start': 0,
        'limit': '20',
        'type': '24',
        'interval_id': '100:90'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    print(list_data)
    fileName = "./豆瓣喜剧类型：" + kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("end...")
