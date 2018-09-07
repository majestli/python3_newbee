#文件上传
#实现方法和其他参数类似，也是构造一个字典然后通过files参数传递

import  requests
files = {"files":open("git.jpeg","rb")}
response =requests.post("http://httpbin.org/post",files=files)
print(response.text)
