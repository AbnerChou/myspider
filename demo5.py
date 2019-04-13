import requests
import re
import json
import time

def get_one_page(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    #print(html)
    results = parse_one_page(html)
    print(next(results))
    for item in results:
        write_to_file(item)


def parse_one_page(html):
    # <dd>.*?board-index.*?>(.*?)</i>.*?date-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
# g = foo()
# print(next(g))
# print("*" * 20)
# print(next(g))

if __name__ == "__main__":
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)