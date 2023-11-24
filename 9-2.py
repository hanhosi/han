""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

print(item)
print(item.get_txt())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text()) """



# select

""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser') """

""" iss = res_html.select("a.wrap_thumb")
# print(iss)

print("\n--------------------------------\n")
for i in iss :
    issue = i.get_text()
    print(issue) """

""" print("\n--------------------------------\n")
ct = res_html.select("a.warp_thumb")
for j in ct :
    # c = j.attrs["data-tiara-custom"]
    c = j.attrs["data-tiara-id"]
    print(c = "\n") """
    
    
    
# 이미지 저장

""" from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

imgs = res_html.select("img")

linkimgs = []

for i in imgs :
    irs = i.attrs["src"]
    linkimgs.append(irs)
    
folder = "imgs/"
if not os.path.isdir(folder) :
    os.mkdir(folder)
    
    
i = 0
for ln in linkimgs :
    if str(ln).find("//t") == False :
        print(ln)
        continue
    else :
        pass
    
    i += 1
    rl(ln, folder + f"{i}.jpg")
    
    # print(ln)
    #linkimgs.append(img.attrs['src]) """
    
    
    
# 시리즈 생성

""" from pandas import Series as sr

date = [10, 20, 30, 40]
sdata = sr(date)

print(sdata) """



# numpy 시리즈 생성

""" from pandas import Series as sr
import numpy as np

# data = np.arange(5)
data = np.arange(1, 5)
sdata = sr(data)

print(sdata)
 """



# 인덱스 확인

from pandas import Serier as sr

data = [10, 20, 30, 40]
sdata = sr(data)

print(sdata.index)
print(sdata.index.tp_list())