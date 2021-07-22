"""
  使用函数来实现
"""
import requests
import time
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

def get_next_link(url):
    # 给出一个链接，返回下一页的链接
    resp = requests.get(url, headers=headers)

    # 将拿到的 URL 解析一下，然后就得到了 html 对象
    html = etree.HTML(resp.text)
    next_link = html.xpath('.//div[@class="page"]/a[contains(@class,"next")]/@href')
    if next_link:
        base_url = 'http://angelimg.spbeen.com'
        next_url = base_url + next_link[0]
        return next_url
    else:
        return False

url = 'http://angelimg.spbeen.com/ang/4394'
while url:
    url = get_next_link(url)
    print(url)
    time.sleep(2)
