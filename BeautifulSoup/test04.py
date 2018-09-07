import requests
import chardet

import  re
from bs4 import BeautifulSoup
# 通过requests获取
#html = requests.get('http://www.pm25.com/xian.html')
#soup = BeautifulSoup(html.text)
# 处理本地文件
#soup = BeautifulSoup(open('test.html'),'lxml')
#print(soup.prettify())
#html=open("test.html")
#print(type(html))

soup=BeautifulSoup(open("test.html",encoding="utf-8"),"lxml")
#print(soup.prettify())
#print(soup.title)
#print(soup.div.get('style'))
#print(soup.div)
#print(soup.div.text)#仅仅是标签内部的文字，不是属性
#print(soup.name)
#print(soup.attrs)
#print(soup)#  BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
#print(soup.head)
#print(soup.a)
#print(soup.p)




print(soup.title.string)

'''tag 的 name与attrs '''
#print(soup.namne)
#print(soup.title.name)


#print(soup.a.attrs)
#print(soup.a['href'])

'''ontent '''
#print(soup.body.contents)
#print(soup.body.contents[1])




'''children'''
"""
for child in soup.body.children:
    print("@@@@@@@@@@@@@ start @@@@@@@@@@@@@@@")
    print(child)
    print("@@@@@@@@@@@@@ end @@@@@@@@@@@@@@@")
"""

""" find all """

'''print(soup.find_all('a'))'''
#
#for tag in soup.find_all(re.compile("^main")):#我们可以利用 soup加标签名轻松地获取这些标签的内容
#    print(tag)

#print(soup.find_all(['title','a']))


#print(soup.find_all(attrs={"class":"title"}))

#print(soup.find_all(text="Python3网络爬虫入门"))

#print(soup.find_all("a", limit=2))

print(soup.find_all(class_="mask"))
