import requests

def get_page():
    url = 'www.baidu.com'
    res = requests.get(url)
    print(res.text)

get_page()
