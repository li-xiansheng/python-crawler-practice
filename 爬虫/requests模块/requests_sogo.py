import requests

if __name__ == '__main__':
    url = "https://www.sogou.com/"
    response = requests.get(url)
    print(response.text)
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    print("end...")
