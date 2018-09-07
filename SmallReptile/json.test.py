import  json

data={
    'no':1,
    'name':'jack',
    'url':'http://www.baidu.com'
}
json_str=json.dumps(data)
print("python原始数据：",repr(data))
print("json 对象",json_str)


#json obj ->python  dict
data2=json.loads(json_str)
print("data2['name']:",data2['name'])
print("data['url']:",data2['url'])
