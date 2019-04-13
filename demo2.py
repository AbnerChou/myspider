import requests

'''直接发送get请求'''


def http_get():
    r = requests.get('http://httpbin.org/get')
    r.encoding = 'utf-8'
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)


'''通过param发送请求'''


def http_param():
    data = {
        'name': 'germey',
        'age': 22
    }

    r = requests.get('http://httpbin.org/get', params=data)
    print(r.url)
    print(r.text)
    print(type(r.text))
    print(r.json())
    print(type(r.json()))


def http_save_binary():
    r = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico','wb') as f:
        f.write(r.content)
    # print(r.text)
    # print(r.content)


def http_save_video():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    r = requests.get("https://www.zhihu.com/explore",headers=headers)
    print(r.text)

if __name__ == "__main__":
    # http_param()
    # http_save_binary()
    http_save_video()
