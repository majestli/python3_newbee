from  urllib import  request
from  urllib import parse
import  json

if __name__ =="__main__":
    Request_URL='http://fanyi.youdao.com/translate'
    Form_Data = {}
   #Form_Data['action'] = 'FY_BY_REALTIME'
   #Form_Data['client']='fanyideskweb'
   #Form_Data['from'] = 'AUTO'

    Form_Data['i']='root'
    Form_Data['doctype'] = 'json'

   #Form_Data['keyfrom'] = 'fanyi.web'
   #Form_Data['salt']='1528946221034'

    #Form_Data['smartresult']='dict'
    #Form_Data['to']='AUTO'
    #Form_Data['typoResult'] = 'false'

    Form_Data['version'] = '2.1'
    #使用urlencode方法转换标准格式
    data=parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
     #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print("翻译的结果是：%s" %translate_results)
#http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
