import requests
from lxml import etree

urls = 'http://angelimg.spbeen.com/ang/10200'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(urls, headers)
html = etree.HTML(response.text)
next_url = html.xpath('.//div[@class="page"]/a/@href')
# print(base_url)
base_url = 'http://angelimg.spbeen.com/'
for link in next_url:
    print(base_url + link)
next_link = html.xpath('.//div[@class="page"]/a[contains(@class,"next")]/@href')
print("next_url =", base_url + next_link[0])