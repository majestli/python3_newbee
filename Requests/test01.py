import requests
response =  requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
##很多情况下的网站如果直接response.text会出现乱码的问题，所以这个使用response.content
##这样返回的数据格式其实是二进制格式，然后通过decode()转换为utf-8，这样就解决了通过response.text直接返回显示乱码的问题.
print(response.content.decode("utf-8"))
