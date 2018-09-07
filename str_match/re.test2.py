import  re
line = 'Cats are smarter than dogs'

matchObj =re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

#()来将我们想要的子字符串括起来，（）实际上就是标记了一个子表达式的开始与结束位置，
#被标记的每个子表示达依次对应每个分组，可以调用group()方法传入分组的索引来提取结果
#group()会输出完整的匹配结果，而group(1)会输出第一个被()包围的匹配结果
#
if matchObj:
    print("matchObj.group:",matchObj.group())
    print("matchObj.group1:",matchObj.group(1))
    print("matchObj.group2:",matchObj.group(2))
else:
    print("No match!!!")
