from urllib import  request



req=request.Request("http://fanyi.baidu.com")
response=request.urlopen(req)


print("geturl打印信息：%s"%(response.geturl()))
print("*************************************")
print("info打印信息：%s"%(response.info()))
print("*************************************")
print("getcode打印信息：%s"%(response.getcode()))
