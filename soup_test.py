# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
r = requests.get("https://www.enterdesk.com/")
# 获取页面内容
content = r.content
# 用html.parser解析html
soup = BeautifulSoup(content, 'html.parser')
# 获取所有class为egene_pic_dl，返回tag类,为list
all = soup.find_all(class_='egeli_pic_dl')
for i in all:
    # 获取图片路径和名称
    img_url = i.img['src']
    img_name = i.img['title']
    # 保存图片
    with open(os.getcwd()+'\\img\\'+img_name+'.jpg', 'wb') as f:
        f.write(requests.get(img_url).content)



