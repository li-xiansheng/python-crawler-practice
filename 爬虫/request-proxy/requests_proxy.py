import requests
#  proxies 参数应用
if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    param = {
        'start': 0,
        'limit': '20',
        'type': '24',
        'interval_id': '100:90'
    }
    response = requests.get(url=url,
                            params=param,
                            headers=headers,
                            proxies={"https", "127.0.0.1:8080"})

    print(response.text)
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print("end...")
