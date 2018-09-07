import  requests

response =requests.get("https://www.zhihu.com")
print(response.text)
#很多情况下的网站如果直接response.text会出现乱码的问题，所以这个使用response.content
#
print(response.content.decode("utf-8"))
