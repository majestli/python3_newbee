from bs4 import  BeautifulSoup
import  parser
import  re
#html为解析的页面获得html信息,为方便讲解，自己定义了一个html文件
#   简单来说，Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据
#    Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#Tag
#NavigableString
#BeautifulSoup
#Comment
html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""
soup =BeautifulSoup(html,'lxml')

#print(soup.prettify())
# Tag通俗点讲就是HTML中的一个个标签 <title>Jack_Cui</title>  上面的title就是HTML标签，标签加入里面包括的内容就是Tag
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)
#  对于Tag，有两个重要的属性：name和attrs
# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称
print(soup.a.attrs)
print(soup.a['class'])
print(soup.a.get('class'))



print("+00000000000000000############################################+")
#既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用 .string
print(soup.title.string)
#BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性：
print(type(soup.name))
print(soup.name)
print(soup.attrs)

#Comment对象是一个特殊类型的NavigableString对象，其实输出的内容仍然不包括注释符号，
# 但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

print(soup.li)
print(soup.li.string)
print(type(soup.li.string))


print("+111111111111111111111############################################+")

print(soup.body)

# tag的content属性可以将tag的子节点以列表的方式输出
print("+1.51.5.1.5.1.5.1.5############################################+")
print(soup.body.contents)#
#print(soup.body.contents[1])

# children 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点，它是一个 list 生成器对象
print("22222222222222222+############################################+")
for child  in soup.body.children:
    print(child.string)

#ind_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件。name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉。
print("+3333333333333333333333############################################+")
print(soup.find_all("a"))

for tag  in soup.find_all(re.compile("^b")):
    print(tag.name)
print(soup.find_all(['titel','b']))


print(soup.find_all("a",limit=2))
print(soup.find_all(class_="title"))
