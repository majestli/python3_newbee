from urllib import  request,parse
import  chardet,json

if __name__=="__main__":
    req_url='http://fanyi.baidu.com/sug'
    Form_Data={"kw":'love'}
    data= parse.urlencode(Form_Data).encode('utf-8')
    response =request.urlopen(req_url,data)
    html=response.read().decode('utf-8')
    print(html)
    translate_results = json.loads(html)
    for item in translate_results['data']:
        for items in item:
            print(item[items])
