import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)
#获取cookie
for key,vaule in response.cookies.items():
    print(key+"="+vaule)


#会话维持 cookie的一个作用就是可以用于模拟登陆，做会话维持


s = requests
s=requests.Session()#第一次则是通过创建一个session对象
s.get("http://httpbin.org/cookies/set/number/123456")
response=s.get("http://httpbin.org/cookies")
print(response.text)


#证书验证
#现在的很多网站都是https的方式访问，所以这个时候就涉及到证书的问题


import urllib3

urllib3.disable_warnings()

response=requests.get("https://www.12306.cn",verify=False)
print(response.status_code)


#代理设置

proxies={
    'http':'106.46.136.112:808',
    "https":"http://127.0.0.1:8888"

}
#response=requests.get("https://www.baidu.com",proxies=proxies)
#print(response.text)

#认证设置
#如果碰到需要认证的网站可以通过requests.auth模块实现
from requests.auth import  HTTPBasicAuth

#异常处理
#关于reqeusts的异常在这里可以看到详细内容：
#http://www.python-requests.org/en/master/api/#exceptions
#所有的异常都是在requests.excepitons中

from   requests.exceptions import  ReadTimeout,ConnectionError,RequestException
try:
    response=requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user","123"),timeout=3)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connect error")
except RequestException:
    print("error")
