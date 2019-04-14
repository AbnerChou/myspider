from bs4 import BeautifulSoup

soup = BeautifulSoup('<p name="nice">Hello</p>','lxml')
print(soup.p.attrs['name'])