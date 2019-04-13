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
        'name':'germey',
        'age':22
    }

    r = requests.get('http://httpbin.org/get',params=data)
    print(r.text)


if __name__ == "__main__":
    http_param()