from lxml import etree


def parse_text():
    text = '''
    <div>
    <ul>
    <li class="item-O"><a href="linkl.html">first item</a><li>
    <li class="item-1"><a href="link2.html">second item</a><lli>
    <li class="item-inactive"><a href="link3.html">third item</a></h>
    <li class="item-1"><a href="link4.html">fourth item</a><lli>
    <li class ＝"item-0"><a href＝"links.html">fifth item</a>
    </ul>
    </div>
    '''
    html = etree.HTML(text)
    print(html)
    result = etree.tostring(html)
    print(result.decode('utf-8'))

def parse_file():
    html = etree.parse('test.html',etree.HTMLParser())
    # result = etree.tostring(html)
    result = html.xpath('//li')
    # print(result.decode('utf-8'))
    print(result)


def parse_child():
    html = etree.parse('test.html',etree.HTMLParser())
    result = html.xpath('//li/a')
    print(result)

def parse_text():
    html = etree.parse('test.html',etree.HTMLParser())
    result = html.xpath('//li[@class="item-O"]//text()')
    print(result)

# parse_file()
# parse_child()
parse_text()