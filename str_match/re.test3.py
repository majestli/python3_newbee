import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
# ? 非贪婪匹配\w匹配字母数字及下划线
#\W匹配非字母数字及下划线
#\s匹配任意空白字符，等价于 [\t\n\r\f].
#\S匹配任意非空字符
#\d匹配任意数字，等价于 [0-9]
#\D匹配任意非数字
#\A匹配字符串开始
#\Z匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
#\z匹配字符串结束
#\G匹配最后匹配完成的位置
#\n匹配一个换行符
#\t匹配一个制表符
# ^匹配字符串的开头
# $匹配字符串的末尾。
# .匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
#[...]用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#[^...]不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
#*匹配0个或多个的表达式。
#+匹配1个或多个的表达式。
#?匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
#{n}精确匹配n个前面表达式。
#{n, m}匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
#a|b匹配a或b
#( )匹配括号内的表达式，也表示一个组
print(result)
print(result.group(1))
print(result.span())

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result1= re.search('Hello.*?(\d+).*?Demo', content)
print(result1)
print(result1.group(1))
