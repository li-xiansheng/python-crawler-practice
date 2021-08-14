import requests

#UA 伪装
if __name__ == '__main__':
    url = "https://www.sogou.com/web"
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url, param,headers = headers)
    print(response.text)
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print("end...")
