#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests

# UA 伪装
if __name__ == '__main__':
    url = "https://fanyi.baidu.com/v2transapi"
    kw = input('enter a word:')
    data = {
        'query': kw,
        'from': 'en',
        'zh': 'zh',
        # "transtype": "enter",
        # "simple_means_flag": 3,
        # "sign": "478531.241266",
        # "token": "ecc90673fa67abb5d5d986e32c60e8f1",
        # "domain": "common"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Tracecode': '07923316260305237770081414',
        'Cookie': 'BIDUPSID=83109694C1E21CFF71516889ABBA408E; BAIDUID=83109694C1E21CFF29A96AAC5CCDEEE1:FG=1; __yjs_duid=1_81eefa1701ee065b406bda003f71fb651628413999073; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1628915430; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1628917626; H_PS_PSSID=31660_26350; delPer=0; PSINO=6; BAIDUID_BFESS=83109694C1E21CFF29A96AAC5CCDEEE1:FG=1; BA_HECTOR=25a1ala52k24a52kgo1ghen7l0q; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1628921562; __yjs_st=2_MzZlOTVhZmEzMWM0MTBkODZhNjYxOGYxMmRjYjM1ODI1ZjcwNjE3M2RiNmNiNDBhMDg5ZmIzZWJkZmUyYWJmYWJhM2FhMzUxYzU0ZDljOThmZmZiNjMzOGUxNTVjOGZiODgxMThkZTc0NTU0Y2Y1MWZlNDEwOWVhNDYxMWYzZTIyZTEzNmNiODZjNzMzZTkxZTk1N2YwN2ZjNjkyM2Q3MmUzZjFmMTExOGRlNzVmN2QxMmNmNGQxY2MyM2UxM2FmN2NjOTJmZDRkNGNmNzY0N2RlODI5MGNjYjExOTczZTY5Y2Q0NmMyMGFlZjkyZGZlNTg5OTlkMjE0MTI1ZDc4NF83XzUzOWE0ZjUw; ab_sr=1.0.1_MGVkM2VmODBhNWQyNGVlNDQ2YTA4YWE2ZmZjNTZkZjI5ZGZiY2JmMjcyMDI1MGUyOTcxYjg4N2Q2ZjExOGRiZmM5YjJkNDk1MjdkYWEwNjA2NGY1ZDRlODAxOGM5MDAzMzNlZTBiZWY4NGVhMWEzZmVjMTA4ZDZkYzkyMzhhYmYxZGFiNGRlOTk3M2YxMTM4YTAzODQ3MjcxZTEyYjFjMw==',
        # 'Host': 'fanyi.baiud.com'
        'X-Requested-With': 'XMLHttpRequest',
        
    }
    response = requests.post(url, data=data, headers=headers)
    dic_obj = response.json()
    print(dic_obj)
    fileName = "./翻译：" + kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print("end...")
