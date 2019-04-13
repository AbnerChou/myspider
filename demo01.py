from selenium import  webdriver
import aiodns
import aiohttp
import lxml
from bs4 import BeautifulSoup
import pyquery
# browser = webdriver.PhantomJS()
# browser.get('http://www.baidu.com')
# print(browser.current_url)

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)
