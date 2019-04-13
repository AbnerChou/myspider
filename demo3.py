import requests
from requests.auth import HTTPBasicAuth

def http_post():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    data = {'name':'germey','age':'22'}
    r = requests.post("http://httpbin.org/post",data=data)
    print(r.text)
    exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

def http_post_file():
    files = {'file':open('favicon.ico','rb')}
    r = requests.post("http://httpbin.org/post",files=files)
    print(r.text)

def http_cookies():
    r = requests.get("https://www.baidu.com")
    print(r.cookies)

def http_login_byCookie():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    cookies = 'l_n_c=1; q_c1=8ec8bdee87794c92a7c4646e3c5cb459|1555150383000|1555150383000; _xsrf=28af0a6e7d82f70f22167a69ca58cf7f; r_cap_id="OTExNzQ1OWM5MTJiNDRjMDk5NzY5Mjg4MmY2NGJjMGQ=|1555150383|7098a4b065ad4c34e5736a5419e09c9511a94a5a"; cap_id="N2ZhODFhNWExMTJmNDljMmFjY2E3YWVlNjY0ZGMwYmU=|1555150383|b803cec124300843e4e7826a8c5b39e816a76646"; l_cap_id="YjQyZTc4NWVkMTcxNDczMjhkOWFkNzIxYWZjYTViY2U=|1555150383|2a97a0b6df2f9d4825b0c96cb4a6aadc76d3a759"; n_c=1; d_c0="ADClcpifRQ-PTuaGzuq4JliVbYpLt_AF_Ug=|1555150386"; __utma=51854390.1180474806.1555150390.1555150390.1555150390.1; __utmc=51854390; __utmz=51854390.1555150390.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190413=1; _zap=beab63a9-48ca-4c9b-9eea-bef631438965; _xsrf=uH2V3iB3pyfryqr3OuCnSPMUpJ6jChW7; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c; capsion_ticket="2|1:0|10:1555152333|14:capsion_ticket|44:NWE2NzM0NjM4NzIzNGEzYTkyMzBmY2RmZDI2MzNjYWY=|942c3424038251b935e4c1cbe2ede56721ec5e811497e0fa7d049092cb9ab755"; z_c0="2|1:0|10:1555152345|4:z_c0|92:Mi4xWldrZkFnQUFBQUFBTUtWeW1KOUZEeVlBQUFCZ0FsVk4yUXVmWFFBMmVlZy1WZlhqQ0tYTnhqSFRXTzBRTldpS3R3|18f4e5810b890d48aaead7b1ca0026fe127e40764b10ff719e1668c669c150c9"'
    jar = requests.cookies.RequestsCookieJar()
    for cookie in cookies.split(';'):
        key,value = cookie.split('=',1)
        jar.set(key,value)
    r = requests.get("http://www.zhihu.com",cookies=jar,headers=headers)
    print(r.text)

def http_auth():
    response = requests.get('https://www.12306.cn')
    print(response.status_code)

def http_proxies():

    proxies={
        "http":"http://10.10.1.10:3128",
        "http":"http://10.10.1.10:1080",
    }

    r = requests.get("https://www.taobao.com",proxies=proxies)
    print(r.text)



if __name__ == "__main__":
    # http_post()
    # http_post_file()
    # http_cookies()
    # http_login_byCookie()
    # http_auth()
    http_proxies()