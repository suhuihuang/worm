"""
links = [1,2,3,4,5,6,7,8,9]
for i in range(3,11):
    links.append(i)
print(links)

links = [1,2,3,4,5,6,7]
for i in range(4,10):
    if i not in links:
        links.append(i)
print(links)
"""
import requests
from lxml import etree
import os

# 1. 以列表的方式来翻页
# 2. 获取当前每页的数据
# 3. 下载当前页的数据到本地

url = 'http://angelimg.spbeen.com/ang/10200/1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Referer': 'http://angelimg.spbeen.com'
}
all_links = [url]
img_links = []
all_imgs = []
title = ""
def get_next_link(url):
    # 给出一个链接，返回下一页的链接
    resp = requests.get(url, headers=headers)
    # 将拿到的 URL 解析一下，然后就得到了 html 对象
    html = etree.HTML(resp.text)
    imgs = html.xpath('.//div[@id="content"]/a/img/@src')
    # print(imgs)
    img_links.extend(imgs)
    global title
    title = html.xpath('.//div[@class="article"]/h2/text()')
    if title:
        title = title[-1]
    all_img=html.xpath('.//img/@src')
    all_imgs.extend(all_img)
    next_link = html.xpath('.//div[@class="page"]/a/@href')
    for i in next_link:
        base_url = 'http://angelimg.spbeen.com'
        next_url = base_url + i
        # print(next_url)
        if next_url not in all_links:
            all_links.append(next_url)


for link in all_links:
    # print("当前请求的链接是：", link)
    get_next_link(link)

# print("当前列表的链接内容为", [i.split('/')[-1] for i in all_links ])
# print("当前图片链接的列表内容为：",len(img_links), img_links)
# print("当前所有的图片:",len(all_imgs), all_imgs)
# print("当前的标题:",title)

if not os.path.exists("imgs/ang"):  # os.path.exists  检查目录是否存在
    os.makedirs("imgs/ang")         # os.makedirs     创建联级目录     os.mkdir  创建单个目录
    os.makedirs('imgs/img')

# for img in img_links:
#     filename = img.split('/')[-1]
#     filepath = 'imgs/ang' + filename
#     resp = requests.get(img, headers=headers)
#     with open(filepath, 'wb') as file:        # 图片是字节，以字节的方式写入
#         file.write(resp.content)              # 字节写入  content

# for img in all_imgs:
#     filename = img.split('/')[-1]
#     filepath = 'imgs/img' + filename
#     resp = requests.get(img, headers=headers)
#     with open(filepath, 'wb') as file:
#         file.write(resp.content)

